import sqlite3

from registry import Settings
from registry.backends.backend import Backend


class SQLite(Backend):
    def __init__(self) -> None:
      connection = sqlite3.connect("terraformregistryapi.db")
      connection.close()

    def read(self):
      pass

    def write(self):
      pass