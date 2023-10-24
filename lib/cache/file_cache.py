import os
import lib.cache.Cache as Cache
import lib.fs.File as File

class FileCache(Cache):
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

    def read(self):
        self._cache = File.absolute(self._path).skel({}).read()

    def write(self):
        print("%s => %s" % (self._path, self._cache))
        File.absolute(self._path).write(self._cache)
