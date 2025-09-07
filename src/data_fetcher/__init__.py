"""
data_fetcher
------------
Library to fetch and process JSON data from public APIs.
"""

__version__ = "0.1.0"

from .fetcher import fetch_json
from .processor import filter_items, extract_field

__all__ = ["fetch_json", "filter_items", "extract_field"]
