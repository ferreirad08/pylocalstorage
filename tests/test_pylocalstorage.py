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
            ("x", 1),
            ("x", "this"),
            ("x", "localhost"),
            ("x", {"name": "Brazil", "population": 215e6}),
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
        assert storage.key(-1) is None
        assert storage.key(storage.length) is None
        assert None not in [storage.key(i) for i in range(storage.length)]
        assert storage.key("anything") is None

    def test_clear(self):
        storage = LocalStorage()
        storage.clear()
        storage.setItem("x", "this")
        assert storage.length > 0
        storage.clear()
        assert storage.key(0) is None
        assert storage.length == 0
