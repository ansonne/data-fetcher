from retry_lib.retry import retry


def test_retry_success():
    calls = {"count": 0}

    @retry(max_retries=3, delay=0.01)
    def func():
        calls["count"] += 1
        return True

    assert func() is True
    assert calls["count"] == 1


def test_retry_fail():
    calls = {"count": 0}

    @retry(max_retries=2, delay=0.01)
    def func():
        calls["count"] += 1
        raise ValueError("Fail")

    import pytest

    with pytest.raises(ValueError):
        func()
    assert calls["count"] == 2
