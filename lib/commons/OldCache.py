import json
import os

class Cache:
    def __init__(self, path: str, always_save: bool = False):
        self._cache = {}
        self._path = path
        self._always_save = always_save
        self.read()

    def set(self, key: str, value):
        self._cache[key] = value
        if self._always_save:
            self.write()

    def get(self, key: str):
        return self._cache.get(key)

    def read(self):
        if os.path.exists(self._path):
            with open(self._path, mode="r", encoding="utf-8") as file:
                self._cache = json.loads(file.read())
        else:
            self._cache = {}
            self.write()

    def write(self):
        with open(self._path, mode="w", encoding="utf-8") as file:
            file.write(json.dumps(self._cache))
