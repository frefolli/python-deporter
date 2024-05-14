from __future__ import annotations
import abc
import deporter.commons.Platform as Platform
import deporter.commons.User as User
import deporter.commons.Repository as Repository
import deporter.commons.Credentials as Credentials

class DB(abc.ABC):
    @staticmethod
    def new(update: bool = False) -> DB:
        import deporter.db.cache_db as impl
        return impl.CacheDB(update=update)

    def __init__(self, update: bool = False):
        self._update = update
        self._context = {}
    
    def platform(self, platform: Platform) -> DB:
        self._context['platform'] = platform
        return self
    
    def user(self, user: User) -> DB:
        self._context['user'] = user
        return self
    
    def credentials(self, credentials: Credentials) -> DB:
        self._context['credentials'] = credentials
        return self
    
    def repository(self, repository: Repository) -> DB:
        self._context['repository'] = repository
        return self
    
    def clear(self) -> DB:
        self._context = {}
        return self

    @abc.abstractmethod
    def get_repositories(self) -> list[Repository]:
        """After resolving this action, calls `DB.clear()`
        """
        pass

    @abc.abstractmethod
    def set_repositories(self, repos: list[Repository]):
        """After resolving this action, calls `DB.clear()`
        """
        pass
