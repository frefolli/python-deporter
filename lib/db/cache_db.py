import lib.db.DB as DB

class CacheDB(DB):
    def __init__(self, update: bool = False):
        super().__init__(update=update)

    @abc.abstractmethod
    def get_repositories(self) -> list[Repository]:
        pass

    @abc.abstractmethod
    def get_repository(self, name: str) -> Repository:
        pass
