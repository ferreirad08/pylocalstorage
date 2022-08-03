"""Tests for LocalStorage."""

from pylocalstorage import LocalStorage, WriteStorageError
import pytest


class TestLocalStorage:

    @pytest.mark.parametrize("value", (int, str,),)
    def test_invalid_value(self, value):
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

    def test_removeItemWithoutExcept(self):
        try:
            storage = LocalStorage()
            storage.setItem("anything", "this")
            storage.removeItem("anything")
            storage.removeItem("anything")
        except:
            assert False
        else:
            assert True

    def test_removeItem(self):
        storage = LocalStorage()
        storage.setItem("x", "this")
        storage.removeItem("x")
        x = storage.getItem("x")
        assert x == None

    def test_key(self):
        storage = LocalStorage()
        storage.setItem("x", "this")
        assert "x" in [storage.key(i) for i in range(storage.length)]

    def test_clear(self):
        storage = LocalStorage()
        storage.setItem("x", "this")
        assert storage.length > 0
        storage.clear()
        assert storage.length == 0
