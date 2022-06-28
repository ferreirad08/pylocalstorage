# localstorage

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ferreirad08/localstorage/blob/main/LICENSE)

## Requirements
* `python 3`

## Examples

    from localstorage import LocalStorage

    # Iniciando um objeto LocalStorage
    local_storage = LocalStorage("./localstorage.json")

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
