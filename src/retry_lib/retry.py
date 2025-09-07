from typing import Callable, Any
import time
import functools


def retry(
    max_retries: int = 3, delay: float = 1.0
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Retry decorator with type hints.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempts += 1
                    if attempts >= max_retries:
                        raise
                    time.sleep(delay)

        return wrapper

    return decorator
