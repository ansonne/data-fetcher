from typing import Any, Dict, Optional
import logging
import requests
from retry_lib.retry import retry

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


@retry(max_retries=3, delay=1)
def fetch_json(url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Fetch JSON data from an API with retry logic.
    """
    logger.info(f"Fetching data from {url} with params {params}")
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data: Dict[str, Any] = response.json()  # no type: ignore
    return data
