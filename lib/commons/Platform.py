import abc
import lib.commons.Credentials as Credentials
import lib.commons.Repository as Repository
import lib.commons.User as User

class Platform(abc.ABC):
    def __init__(self, url: str):
        self._url = url

    @abc.abstractmethod
    def get_user_repositores(self, user: User, credentials: Credentials) -> list[Repository]:
        pass

    @abc.abstractmethod
    def migrate_repository(self, repo: Repository, config: dict, credentials: Credentials) -> Repository:
        pass

    def get_url(self) -> str:
        return self._url

    def __repr__(self) -> str:
        return self.get_url()
