import lib.db.DB as DB
import lib.commons.Repository as Repository
import lib.commons.datetime as datetime

class CacheDB(DB):
    def __init__(self, update: bool = False):
        super().__init__(update=update)
        self._cache = Cache.new('.cache.yml', eager=False)

    @abc.abstractmethod
    def get_repositories(self) -> list[Repository]:
        url = self._context['platform'].get_url()
        username = self._context['user'].get_username()
        credentials = self._context['credentials']
        
        if url not in self._cache:
            self._cache[url] = {}
        user = self._context['user']
        
        if username not in self._cache[url]:
            self._cache[url][username] = {}
        
        if ('repos' in self._cache[url][username]):
            repos = self._cache[url][username]['repos']
            if not datetime.is_old(repos['updated_at']):
                return [Repository.from_dict(repo) for repo in repos['data'].values()]

        repos = {
            'updated_at': datetime.now()
            'data': {}
        }
        for repo in platform.get_user_repositories(user, credentials):
            repos['data'][repo.name] = repo.to_dict()
        self._cache[url][username]['repos'] = repos
        self._cache.write()
        self.clear()
        return [Repository.from_dict(repo) for repo in repos['data'].values()]
