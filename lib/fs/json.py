from __future__ import annotations
import lib.fs.File as File
import json
import os

class Json(File):
    @staticmethod
    def relative(base: str, path: str) -> Json:
        return Json(os.path.join(base, path))

    @staticmethod
    def absolute(path: str) -> Json:
        return Json(path)

    def __init__(self, path: str):
        self._path = path
        self._skel = None

    def skel(self, skel) -> Json:
        self._skel = skel
        return self

    def read(self) -> dict:
        if os.path.exists(self._path):
            with open(self._path, mode="r", encoding="utf-8") as file:
                return json.loads(file.read())
        elif self._skel is not None:
            self.write(self._skel)
            return self._skel
        else:
            raise Exception("no '%s' file exists nor skel has been defined" % self._path)

    def write(self, obj):
        with open(self._path, mode="w", encoding="utf-8") as file:
            file.write(json.dumps(obj))
