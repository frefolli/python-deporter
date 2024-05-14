import json
import os
import deporter.cache.Cache as Cache
import deporter.utils as utils

@utils.deprecated("Use deporter.cache.Cache instead")
class OldCache(Cache):
    def __init__(self, path: str, eager: bool = False):
        super().__init__(path, eager)
        self._cache = {}
        self.read()

    def set(self, key: str, value):
        self._cache[key] = value
        if self._eager:
            self.write()

    def get(self, key: str):
        return self._cache.get(key)

    def has(self, key: str) -> bool:
        return key in self._cache

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
