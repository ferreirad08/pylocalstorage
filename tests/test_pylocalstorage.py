from pylocalstorage import LocalStorage


class TestLocalStorage:

    def test_setItem(self):
        storage = LocalStorage()
        storage.setItem("x", "this")
        x = storage.getItem("x")
        assert x == "this"

    def test_removeItem(self):
        storage = LocalStorage()
        storage.setItem("x", "this")
        storage.removeItem("x")
        x = storage.getItem("x")
        assert x == None
