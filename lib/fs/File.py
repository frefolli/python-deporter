from __future__ import annotations
import os
import abc

class File(abc.ABC):
    @staticmethod
    def file_ext(path: str) -> str:
        return path.split(os.path.extsep)[-1]
    @staticmethod
    def relative(base: str, path: str) -> File:
        return File.absolute(os.path.join(base, path))

    @staticmethod
    def absolute(path: str) -> File:
        ext = File.file_ext(path)
        if ext == "yml":
            import lib.fs.yaml as impl_yaml
            return impl_yaml.Yaml.absolute(path)
        elif ext == "json":
            import lib.fs.json as impl_json
            return impl_json.Json.absolute(path)
        else:
            raise Exception("unknown file extension '%s'" % ext)

    @abc.abstractmethod
    def skel(self, skel) -> File:
        pass

    @abc.abstractmethod
    def read(self) -> dict:
        pass

    @abc.abstractmethod
    def write(self, obj):
        pass
