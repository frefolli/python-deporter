from __future__ import annotations
import json
import os
import abc

class Cache(abc.ABC):
    @staticmethod
    def new(path: str = ".cache.yml", eager: bool = False) -> Cache:
        import lib.cache.file_cache as impl_file
        return impl_file.FileCache(path, eager)

    def __init__(self, path: str, eager: bool = False):
        self._path = path
        self._eager = eager

    @abc.abstractmethod
    def set(self, key: str, value):
        pass

    @abc.abstractmethod
    def get(self, key: str):
        pass

    @abc.abstractmethod
    def has(self, key: str) -> bool:
        pass

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass
