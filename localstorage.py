import json


class LocalStorage:

    fname = "localstorage.json"
    length = 0

    def __init__(self):
        self.write_json({})

    def setItem(self, key, value):
        data = self.read_json()
        data[key] = value
        self.write_json(data)

    def getItem(self, key):
        data = self.read_json()
        return data.get(key)

    def removeItem(self, key):
        data = self.read_json()
        del data[key]
        self.write_json(data)

    def clear(self):
        self.write_json({})

    def key(self, index):
    	data = self.read_json()
    	return list(data.keys())[index]

    def read_json(self):
        with open(self.fname, "r") as file:
            return json.load(file)

    def write_json(self, data):
        with open(self.fname, "w") as file:
            print(json.dumps(data), file=file)
        self.length = len(data)


if __name__ == "__main__":

    # Iniciando um objeto LocalStorage
    local_storage = LocalStorage()

    # Criando três itens
    local_storage.setItem("name", "David")
    local_storage.setItem("country", "Brazil")
    local_storage.setItem("city", "Manaus")
    print(local_storage.length)

    # Atualizando um item
    local_storage.setItem("name", "David Ferreira")

    # Obtendo um item
    print(local_storage.getItem("name"))

    # Removendo um item
    local_storage.removeItem("city")
    print(local_storage.getItem("city"))

    # Recuperando todas as chaves existentes
    for i in range(local_storage.length):
        print(local_storage.key(i))

    # Limpando o LocalStorage
    local_storage.clear()
    print(local_storage.length)
