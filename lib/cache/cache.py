from __future__ import annotations
import json
import os
import abc
import lib.cache.impl.FileCache

class Cache(abc.ABC):
    @staticmethod
    def new(path: str, eager: bool = False) -> Cache:
        return FileCache(path, eager)

    def __init__(self, path: str, eager: bool = False):
        self._path = path
        self._eager = False

    @abc.abstractmethod
    def set(self, key: str, value):
        pass

    @abc.abstractmethod
    def get(self, key: str):
        pass

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass
