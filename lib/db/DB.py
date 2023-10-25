from __future__ import annotations
import abc
import lib.commons.Platform as Platform
import lib.commons.User as User
import lib.commons.Repository as Repository

class DB(abc.ABC):
    @staticmethod
    def new() -> DB:
        return None

    def __init__(self, update: bool = False):
        self._update = update
        self._context = {}
    
    def platform(self, platform: Platform) -> DB:
        self._context['platform'] = platform
    
    def user(self, user: User) -> DB:
        self._context['user'] = user
    
    def repository(self, repository: Repository) -> DB:
        self._context['repository'] = repository
    
    def clear(self) -> DB:
        self._context = {}

    @abc.abstractmethod
    def get_repositories(self) -> list[Repository]:
        """After resolving this action, calls `DB.clear()`
        """
        pass
