# Pylocalstorage

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ferreirad08/pylocalstorage/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/pylocalstorage.svg)](https://badge.fury.io/py/pylocalstorage)
![Tests](https://github.com/ferreirad08/pylocalstorage/actions/workflows/tests.yml/badge.svg)
![Custom badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fjsonblob.com%2Fapi%2FjsonBlob%2F1109252544634568704)
![GitHub issues](https://img.shields.io/github/issues-raw/ferreirad08/pylocalstorage)
[![Downloads](https://pepy.tech/badge/pylocalstorage)](https://pepy.tech/project/pylocalstorage)
[![Downloads](https://pepy.tech/badge/pylocalstorage/month)](https://pepy.tech/project/pylocalstorage)
[![Supported versions](https://img.shields.io/pypi/pyversions/pylocalstorage.svg)](https://pypi.org/project/pylocalstorage)

A package to store data on the hard disk (HD) and make it available to all Python applications running locally!

Version based on the [pickle module](https://docs.python.org/3/library/pickle.html). The pickle module implements binary protocols for serializing and de-serializing a Python object structure.

## Installation

Simply install **pylocalstorage** package from [PyPI](https://pypi.org/project/pylocalstorage/)

```bash
$ pip install pylocalstorage
```

## Examples

```python
>>> from pylocalstorage import LocalStorage
>>> ls = LocalStorage()
>>> ls.setItem("name", "David")
>>> ls.setItem("age", 29)
>>> ls.setItem("address", {"country": "Brazil", "city": "Manaus"})
>>> ls.length
3
>>> ls.setItem("name", "David Ferreira")
>>> ls.getItem("name")
'David Ferreira'
>>> ls.removeItem("name")
>>> for i in range(ls.length):
...     print(ls.key(i))
...
'age'
'address'
>>> ls.clear()
>>> ls.length
0
```
