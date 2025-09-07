from data_fetcher.processor import filter_items, extract_field


def test_filter_items():
    items = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
    filtered = filter_items(items, "id", 1)
    assert filtered == [{"id": 1, "name": "A"}]


def test_extract_field():
    items = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
    names = extract_field(items, "name")
    assert names == ["A", "B"]
