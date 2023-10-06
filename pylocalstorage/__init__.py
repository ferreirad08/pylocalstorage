try:
    import sqlalchemy
except:
    from os import system
    system("pip install SQLAlchemy")

from .pylocalstorage import LocalStorage, WriteStorageError
