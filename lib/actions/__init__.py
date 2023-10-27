import lib.commons.Repository as Repository
import lib.commons.User as User
import lib.commons.Platform as Platform
import logging

def use_cached_repositories(repos, platform, user, as_dict: bool = False):
    logging.info("using cached repositories of [%s][%s]" % (platform, user))
    if not as_dict:
        repos = Repository.from_dict_list(repos)
    return repos

def get_repositories_from_platform(platform, user, credentials, as_dict: bool = False):
    logging.info("querying repositories from [%s][%s]" % (platform, user))
    repos = platform.get_user_repositores(user, credentials)
    if as_dict:
        repos = Repository.to_dict_list(repos)
    return repos

def read_profile(profile: dict) -> dict:
    read = {}
    if 'username' in profile:
        read['user'] = User(username=profile['username'])
    if 'token' in profile and 'user' in read:
        read['credentials'] = read['user'].authenticate(profile['token'])
    if 'platform' in profile:
        read['platform'] = Platform.from_dict(profile['platform'])
    return read

def migrate_repository(source: dict, destination: dict, repository: Repository, config: dict = {}) -> Repository | None:
    logging.info("Migrating '%s' from %s to %s" % (repository, source['platform'], destination['platform']))
    result = destination["platform"].migrate_repository(repository, config, destination["credentials"])
    if result is None:
        logging.error("unable to migrate '%s'" % (repository))
    return result

def migrate_repositories(source: dict, destination: dict, repositories: list[Repository], config: dict = {}) -> list[Repository]:
    logging.info("Migrating %s repositories from %s to %s" % (len(repositories), source['platform'], destination['platform']))
    results = []
    for repo in repositories:
        result = migrate_repository(source, destination, repo, config)
        if result is not None:
            results.append(result)
    return results

def delete_repository(target: dict, repository: Repository) -> Repository | None:
    logging.info("Deleting '%s' from %s" % (repository, target['platform']))
    result = target["platform"].delete_repository(repository, target["credentials"])
    if not result:
        logging.error("unable to delete '%s'" % (repository))
        return repository

def delete_repositories(target: dict, repositories: list[Repository]) -> list[Repository]:
    """Returns the list of Repository which it could delete during the action
    """
    logging.info("Deleting %s repositories from %s" % (len(repositories), target['platform']))
    results = []
    for repo in repositories:
        result = delete_repository(target, repo)
        if result is not None:
            results.append(result)
    return results
