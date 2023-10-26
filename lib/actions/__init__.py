import lib.commons.Repository

def use_cached_repositories(repos, platform, user, as_dict: bool = False):
    logging.info("using cached repositories of %s@%s" % (platform, user))
    if not as_dict:
        repos = Repository.from_dict_list(repos)
    return repos

def get_repositories_from_platform(platform, user, credentials, as_dict: bool = False):
    logging.info("querying repositories from %s@%s" % (platform, user))
    repos = platform.get_user_repositores(user, credentials)
    if not as_dict:
        repos = Repository.from_dict_list(repos)
    return repos

def migrate_repository(source: dict, destination: dict, repository: Repository) -> Repository:
    pass

def migrate_repositories(source: dict, destination: dict) -> list[Repository]:
    pass

def mirror_repository(source: dict, destination: dict, repository: Repository) -> Repository:
    pass

def mirror_repositories(source: dict, destination: dict) -> list[Repository]:
    pass

def read_profile(profile: dict) -> dict:
    read = {}
    if 'username' in profile:
        read['user'] = User(username=profile['username'])
    if 'token' in profile and 'user' in read:
        read['credentials'] = read['user'].authenticate(profile['token'])
    if 'platform' in profile:
        read['platform'] = Platform.from_dict(profile['platform'])
    return read
