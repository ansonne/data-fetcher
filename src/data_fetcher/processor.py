from typing import Any, List, Dict


def filter_items(
    items: List[Dict[str, Any]], key: str, value: Any
) -> List[Dict[str, Any]]:
    return [item for item in items if item.get(key) == value]


def extract_field(items: List[Dict[str, Any]], key: str) -> List[Any]:
    return [item.get(key) for item in items if key in item]
