"""
This file contains a set of utility functions used by the scraper. 
It is generally common practice to separate out common utilities that
are used by all parts of your program as helpers, instead having one
individually across different source files.
"""

from bs4 import BeautifulSoup
import json


def get_next_data(soup: BeautifulSoup) -> dict:
    """Retrieve application-wide data from a Next.js (React) page.

    Args:
        soup (BeautifulSoup): soupified HTML

    Returns:
        dict: parsed JSON data
    """
    # Select the element with `id` of `__NEXT_DATA__`
    return json.loads(soup.select_one("#__NEXT_DATA__").text)