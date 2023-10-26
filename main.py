#!/usr/bin/env python
import lib.commons.Gitea as Gitea
import lib.commons.Github as Github
import lib.commons.Credentials as Credentials
import lib.commons.User as User
import lib.cache.Cache as Cache
import lib.commons.Repository as Repository
import lib.cli.Cli as Cli
import coloredlogs, logging
coloredlogs.install()

def migrate_repositories(source, destination):
    cache = Cache.new(".cache.yml", eager = True)
    repositories = get_cached_repositories(cache)
    if repositories is None:
        logging.info("Fetching %s for repositories ..." % source["platform"])
        repositories = source["platform"].get_user_repositores(source["user"], source["credentials"])
        cache_repositories(cache, repositories)
    logging.info("Migrating %s repositories ..." % (len(repositories)))

    logging.info("from %s@%s, to %s@%s" % (source["platform"],
                                    source["user"],
                                    destination["platform"],
                                    destination["credentials"]))
    for repo in repositories:
        result = destination["platform"].migrate_repository(repo, destination["config"], destination["credentials"])
        if result is not None:
            logging.info("%s => %s" % (repo, result))

def migrate():
    gitea = Gitea.from_env("REFOLINUX")
    github = Github()

    github_creds = Credentials.from_env("FREFOLLI_GITHUB")
    gitea_creds = Credentials.from_env("FREFOLLI_GITEA")

    github_user = User("frefolli")
    gitea_user = User("frefolli")

    migration = {
        "source": {
            "platform": github,
            "user": github_user,
            "credentials": github_creds
        },
        "destination": {
            "platform": gitea,
            "config": {},
            "credentials": gitea_creds
        }
    }
    migrate_repositories(migration["source"], migration["destination"])

if __name__ == "__main__":
    config = Cli.run()
    print(config)
