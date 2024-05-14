from __future__ import annotations
import abc
import deporter.commons.Credentials as Credentials
import deporter.commons.Repository as Repository
import deporter.commons.User as User

class Platform(abc.ABC):
    @staticmethod
    def from_dict(platform: dict) -> Platform:
        import deporter.commons.Gitea
        import deporter.commons.Github
        if platform['name'] == 'github':
            return deporter.commons.Github()
        elif platform['name'] == 'gitea':
            return deporter.commons.Gitea(instance=platform['url'])
        else:
            raise Exception("unknown platform name '%s'" % platform['name'])

    def __init__(self, url: str):
        self._url = url

    @abc.abstractmethod
    def get_user_repositores(self, user: User, credentials: Credentials) -> list[Repository]:
        pass

    @abc.abstractmethod
    def migrate_repository(self, repo: Repository, config: dict, credentials: Credentials) -> Repository:
        pass

    @abc.abstractmethod
    def delete_repository(self, repo: Repository, credentials: Credentials) -> bool:
        pass

    def get_url(self) -> str:
        return self._url

    def __repr__(self) -> str:
        return self.get_url()
