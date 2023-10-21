import abc
import lib.commons.Credentials as Credentials
import lib.commons.Repository as Repository

class Platform(abc.ABC):
    def __init__(self, url: str):
        self._url = url

    @abc.abstractmethod
    def get_repositories_of_user(self, credentials: Credentials) -> list[Repository]:
        pass

    def get_url(self) -> str:
        return self._url

    def __repr__(self) -> str:
        return self.get_url()
