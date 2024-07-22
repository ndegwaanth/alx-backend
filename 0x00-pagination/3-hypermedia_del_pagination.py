#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get a page of the dataset using the index for pagination
        """
        # Assert that index is valid
        assert index is None or isinstance(index, int) and index >= 0

        # Fetch the indexed dataset
        indexed_dataset = self.indexed_dataset()

        # Initialize page data and next index
        data = []
        next_index = index + page_size if index is not None else 0

        # Collect data for the page, skip deleted entries
        current_index = index if index is not None else 0
        while len(data) < page_size and current_index in indexed_dataset:
            data.append(indexed_dataset[current_index])
            current_index += 1

        # Prepare the result dictionary
        return {
            'index': index if index is not None else 0,
            'next_index': next_index if len(data) == page_size else None,
            'page_size': len(data),
            'data': data
        }
