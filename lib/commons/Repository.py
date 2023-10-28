from __future__ import annotations
import re

class Repository:
    @staticmethod
    def from_html_url(html_url: str) -> Repository:
        full_name = "/".join(html_url.strip("/").split("/")[-2:])
        name = full_name.split("/")[1]
        return Repository(name, full_name, html_url)

    @staticmethod
    def from_dict(data: dict) -> Repository:
        return Repository(data["name"],
                          data["full_name"],
                          data["html_url"])

    @staticmethod
    def from_dict_list(data: list[dict]) -> list[Repository]:
        return list(map(Repository.from_dict, data))

    @staticmethod
    def to_dict_list(data: list[Repository]) -> list[dict]:
        return list(map(Repository.to_dict, data))

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

    def to_dict(self) -> dict:
        return {"name": self.get_name(),
                "full_name": self.get_full_name(),
                "html_url": self.get_url()}
