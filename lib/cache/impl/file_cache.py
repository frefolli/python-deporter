import json
import os
import lib.cache.Cache as Cache

class FileCache(Cache):
    def __init__(self, path: str, eager: bool = False):
        super().__init__(path, eager)
        self._cache = {}
        self.read()

    def set(self, key: str, value):
        self._cache[key] = value

    def get(self, key: str):
        return self._cache.get(key)

    def read(self):
        self._cache = File.absolute(path).skel({}).read()

    def write(self):
        File.absolute(path).write(self._cache)
