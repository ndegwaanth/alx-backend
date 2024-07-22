#!/usr/bin/env python3
"""0. Simple helper function"""


def index_range(page, page_size):
    """
    Function should return a tuple of size two containing
    a start index and an end index corresponding to the
    range of indexes to return in a list for those particular
    pagination parameters.

    Parameters:
    page: This is the current page
    page_size: This is the total number of pages

    return: A list for those particular pigination parameter
    """

    start_page = (page - 1) * page_size
    end_page = start_page + page_size

    return (start_page, end_page)
