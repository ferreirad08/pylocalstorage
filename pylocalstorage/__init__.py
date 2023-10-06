try:
    import sqlalchemy
except:
    from os import system
    system("pip install SQLAlchemy")

from .local_storage import LocalStorage
from .exceptions import WriteStorageError
