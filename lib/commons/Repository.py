from __future__ import annotations

class Repository:
    @staticmethod
    def from_json(data: dict) -> Repository:
        return Repository(data["name"],
                          data["full_name"],
                          data["html_url"])

    def __init__(self,
                 name: str,
                 full_name: str,
                 url: str):
        self._name = name
        self._full_name = full_name
        self._url = url

        def get_name(self) -> str:
            return self._name

        def get_full_name(self) -> str:
            return self._full_name

        def get_url(self) -> str:
            return self._url

        def __repr__(self) -> str:
            return self.get_full_name()
