from unittest.mock import patch
from data_fetcher import fetch_json


@patch("data_fetcher.fetcher.requests.get")
def test_fetch_json(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"id": 1, "name": "Test"}

    result = fetch_json("http://fakeapi.com")
    assert result == {"id": 1, "name": "Test"}
