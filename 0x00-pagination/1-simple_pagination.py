#!/usr/bin/env python3
"""0. Simple helper function"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of the dataset
        """
        # Assert that page and page_size are integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculate the start and end index using index_range
        start_index, end_index = self.index_range(page, page_size)

        # Fetch the dataset
        dataset = self.dataset()

        # Return the appropriate page of the dataset
        # or an empty list if out of range
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        Function should return a tuple of size two containing
        a start index and an end index corresponding to the
        range of indexes to return in a list for those particular
        pagination parameters.

        Parameters:
        page: This is the current page
        page_size: This is the total number of pages

        return: A tuple with start index and end index
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return start_index, end_index
