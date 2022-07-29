"""Tests for LocalStorage."""

from pylocalstorage import LocalStorage
import pytest


class TestLocalStorage:

    @pytest.mark.parametrize(
        "exception, value",
        (
            (WriteStorageError, int),
            (WriteStorageError, str),
        ),
    )
    def test_invalid_value(self, exception, value):
        try:
            storage = LocalStorage()
            storage.setItem("x", value)
        except Exception as err:
            assert isinstance(err, WriteStorageError)

    @pytest.mark.parametrize(
        "key, value",
        (
            ("x", "this"),
            ("x", "localhost"),
        ),
    )
    def test_setItem(self, key, value):
        storage = LocalStorage()
        storage.setItem(key, value)
        x = storage.getItem(key)
        assert x == value

    def test_removeItem(self):
        storage = LocalStorage()
        storage.setItem("x", "this")
        storage.removeItem("x")
        x = storage.getItem("x")
        assert x == None
