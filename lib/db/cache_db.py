import lib.db.DB as DB
import lib.commons.Repository as Repository
import lib.commons.datetime as datetime
import lib.actions as actions
#TODO: unify access to actions or abstractions
#TODO: simplify program flow

class CacheDB(DB):
    def __init__(self, update: bool = False):
        super().__init__(update=update)
        self._cache = Cache.new('.cache.yml', eager=False)

    def get_repositories(self) -> list[Repository]:
        platform = self._context['platform']
        url = platform.get_url()
        username = self._context['user'].get_username()
        credentials = self._context['credentials']
        
        if url not in self._cache:
            self._cache[url] = {}
        user = self._context['user']
        
        if username not in self._cache[url]:
            self._cache[url][username] = {}
        
        if ((self._update)
            or ('repos' not in self._cache[url][username])
            or (datetime.is_old(self._cache[url][username]['repos']['updated_at']))):
            self._cache[url][username]['repos'] = {
                'updated_at': datetime.now()
                'data': actions.get_repositories_from_platform(
                    platform=platform,
                    user=platform,
                    credentials=credentials,
                    as_dict=True
                )
            }

        return actions.use_cached_repositories(
            repos=self._cache[url][username]['repos']['data']
            platform=platform,
            user=platform
        )
