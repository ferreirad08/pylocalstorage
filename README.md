# pylocalstorage

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ferreirad08/pylocalstorage/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/pylocalstorage.svg)](https://badge.fury.io/py/pylocalstorage)
![Tests](https://github.com/ferreirad08/pylocalstorage/actions/workflows/tests.yml/badge.svg)
![Custom badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fjsonblob.com%2Fapi%2FjsonBlob%2F1002315458195767296)
[![Downloads](https://pepy.tech/badge/pylocalstorage/month)](https://pepy.tech/project/pylocalstorage)

A package to store data on the hard disk (HD) and make it available to all Python applications running locally!

## Requirements
* `Python 2.7 or higher`

## Installation

Simply install pylocalstorage package from [PyPI](https://pypi.org/project/pylocalstorage/)

    pip install pylocalstorage

## Examples

    from pylocalstorage import LocalStorage

    # Connecting to LocalStorage
    my_storage = LocalStorage()

    # Creating three items
    my_storage.setItem("name", "David")
    my_storage.setItem("age", 29)
    my_storage.setItem("address", {
        "country": "Brazil",
        "city": "Manaus"
    })
    print("Number of items:", my_storage.length)

    # Updating an item
    my_storage.setItem("name", "David Ferreira")

    # Getting an item
    print(my_storage.getItem("name"))

    # Removing an item
    my_storage.removeItem("name")

    # Retrieving all existing keys
    for i in range(my_storage.length):
        print(my_storage.key(i))

    # Cleaning up LocalStorage
    my_storage.clear()
    print("Number of items:", my_storage.length)

