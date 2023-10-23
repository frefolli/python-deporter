from __future__ import annotations
import lib.fs.Yaml.Yaml as Yaml
import lib.fs.Json.Json as Json
import os

class File:
    @staticmethod
    def file_ext(path: str) -> str:
        path.split(os.path.extsep)[-1]
    @staticmethod
    def relative(base: str, path: str) -> File:
        return File.absolute(os.path.join(base, path))

    @staticmethod
    def absolute(path: str) -> File:
        ext = File.file_ext(path)
        if ext == "yml":
            return Yaml.absolute(path)
        elif ext == "json":
            return Json.absolute(path)
        else:
            raise Exception("unknown file extension '%s'" % ext)

    @abc.abstractmethod
    def skel(self, klass) -> File:
        pass

    @abc.abstractmethod
    def read(self) -> dict:
        pass

    @abc.abstractmethod
    def write(self, obj):
        pass
