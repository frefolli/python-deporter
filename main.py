#!/usr/bin/env python
import lib.cli.Cli as Cli
import lib.fs.File as File
import lib.db.DB as DB
import lib.actions as actions
import coloredlogs
coloredlogs.install()

def do_list(config):
    profile = actions.read_profile(File.absolute(config.source).read())
    local_db = DB.new(config.update_db)
    repos = (local_db.platform(profile['platform'])
                     .user(profile['user'])
                     .credentials(profile['credentials'])
                     .get_repositories())
    for repo in repos:
        print(repo)

def do_migrate(config):
    source = actions.read_profile(File.absolute(config.source).read())
    local_db = DB.new(config.update_db)
    repos = (local_db.platform(source['platform'])
                     .user(source['user'])
                     .credentials(source['credentials'])
                     .get_repositories())
    
    if config.destination is not None:
        destination = actions.read_profile(File.absolute(config.destination).read())
        repos = actions.migrate_repositories(source, destination, repos, {
            "mirror": False,
            "private": config.private,
            "wiki": config.wiki
        })
        (local_db.clear()
                 .platform(destination['platform'])
                 .user(destination['user'])
                 .credentials(destination['credentials'])
                 .set_repositories(repos))
    
    if config.mirror is not None:
        mirror = actions.read_profile(File.absolute(config.mirror).read())
        repos = actions.migrate_repositories(source, mirror, repos, {
            "mirror": True,
            "private": config.private,
            "wiki": config.wiki
        })
        (local_db.clear()
                 .platform(mirror['platform'])
                 .user(mirror['user'])
                 .credentials(mirror['credentials'])
                 .set_repositories(repos))

    if config.destination is None and config.mirror is None:
        logging.error("should specify at least a destination or a mirror for the migration to happen")

def do_delete(config):
    target = actions.read_profile(File.absolute(config.source).read())
    local_db = DB.new(config.update_db)
    repos = (local_db.platform(target['platform'])
                     .user(target['user'])
                     .credentials(target['credentials'])
                     .get_repositories())
    
    actions.delete_repositories(target, repos)
    (local_db.clear()
             .platform(target['platform'])
             .user(target['user'])
             .set_repositories([]))

if __name__ == "__main__":
    config = Cli.run()
    
    if config.verb == 'list':
        do_list(config)
    elif config.verb == 'migrate':
        do_migrate(config)
    elif config.verb == 'delete':
        do_delete(config)
