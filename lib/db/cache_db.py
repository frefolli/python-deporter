import lib.db.DB as DB
import lib.cache.Cache as Cache
import lib.commons.Repository as Repository
import lib.datetime as datetime
import lib.actions as actions
import logging

class CacheDB(DB):
    def __init__(self, update: bool = False):
        super().__init__(update=update)
        self._cache = Cache.new('.cache.yml', eager=False)

    def get_repositories(self) -> list[Repository]:
        platform = self._context['platform']
        url = platform.get_url()
        username = self._context['user'].get_username()
        credentials = self._context['credentials']
        
        if not self._cache.has(url):
            self._cache.set(url, {})
        user = self._context['user']
        
        if username not in self._cache.get(url):
            self._cache.get(url)[username] = {}
        
        if ((self._update)
            or ('repos' not in self._cache.get(url)[username])
            or (datetime.is_old(self._cache.get(url)[username]['repos']['updated_at']))):
            self.set_repositories(actions.get_repositories_from_platform(platform=platform,
                                                                         user=user,
                                                                         credentials=credentials))

        return actions.use_cached_repositories(
            repos=self._cache.get(url)[username]['repos']['data'],
            platform=platform,
            user=platform
        )

    def set_repositories(self, repos: list[Repository]):
        platform = self._context['platform']
        url = platform.get_url()
        username = self._context['user'].get_username()
        
        if not self._cache.has(url):
            self._cache.set(url, {})
        user = self._context['user']
        
        if username not in self._cache.get(url):
            self._cache.get(url)[username] = {}

        logging.info("caching repositories for [%s][%s]" % (
            platform, user
        ))
        self._cache.get(url)[username]['repos'] = {
            'updated_at': datetime.now(),
            'data': Repository.to_dict_list(repos)
        }
        self._cache.write()
