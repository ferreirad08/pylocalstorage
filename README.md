# pylocalstorage

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ferreirad08/pylocalstorage/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/pylocalstorage.svg)](https://badge.fury.io/py/pylocalstorage)
![Tests](https://github.com/ferreirad08/pylocalstorage/actions/workflows/tests.yml/badge.svg)
$(https://jsonblob.com/api/jsonBlob/1002315458195767296)
<!--#
NOUN=mother
ATTRIBUTION=Mark Wahlberg
$-->
{{ NOUN }}
[![coverage](https://img.shields.io/badge/coverage-85%25-yellow)](https://github.com/ferreirad08/pylocalstorage/runs/7567830488?check_suite_focus=true)

A package to store data on hard disk (HD) and make it available to all Python applications running in parallel!

## Requirements
* `python 3`

## Installation

Simply install pylocalstorage package from [PyPI](https://pypi.org/project/pylocalstorage/)

    pip install pylocalstorage

## Examples

    from pylocalstorage import LocalStorage

    # Conectando ao LocalStorage
    my_storage = LocalStorage()

    # Criando três itens
    my_storage.setItem("name", "David")
    my_storage.setItem("country", "Brazil")
    my_storage.setItem("city", "Manaus")
    print(my_storage.length)

    # Atualizando um item
    my_storage.setItem("name", "David Ferreira")

    # Obtendo um item
    print(my_storage.getItem("name"))

    # Removendo um item
    my_storage.removeItem("city")
    print(my_storage.getItem("city"))

    # Recuperando todas as chaves existentes
    for i in range(my_storage.length):
        print(my_storage.key(i))

    # Limpando o LocalStorage
    my_storage.clear()
    print(my_storage.length)
