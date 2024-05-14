#!/usr/bin/env python
import deporter.cli.Cli as Cli
import deporter.fs.File as File
import deporter.db.DB as DB
import deporter.actions as actions
import deporter.commons.Repository as Repository
import coloredlogs
import logging
import os
coloredlogs.install()

def GetSourceFile(ID: str):
    source_dir = os.path.expanduser('~/.config/python-deporter/sources')
    if not os.path.exists(source_dir):
        logging.debug("Creating source_dir: '%s'" % source_dir)
        os.system("mkdir -p %s" % source_dir)
    source_file_path = os.path.join(source_dir, "%s.yml" % ID)
    if not os.path.exists(source_file_path):
        raise Exception("source file path '%s' doesn't exists" % source_file_path)
    return source_file_path

def do_list(config):
    profile = actions.read_profile(File.absolute(GetSourceFile(config.source)).read())
    local_db = DB.new(config.update_db)
    repos = (local_db.platform(profile['platform'])
                     .user(profile['user'])
                     .credentials(profile['credentials'])
                     .get_repositories())
    for repo in repos:
        print(repo)

def do_migrate(config):
    source = actions.read_profile(File.absolute(GetSourceFile(config.source)).read())
    local_db = DB.new(config.update_db)
    repos = []

    if config.target:
        repos = [Repository.from_html_url(config.target)]
    else:
        repos = (local_db.platform(source['platform'])
                         .user(source['user'])
                         .credentials(source['credentials'])
                         .get_repositories())
    
    if config.destination is not None:
        destination = actions.read_profile(File.absolute(GetSourceFile(config.destination)).read())
        repos = actions.migrate_repositories(source, destination, repos, {
            "mirror": False,
            "private": config.private,
            "wiki": config.wiki
        })
    
    if config.mirror is not None:
        mirror = actions.read_profile(File.absolute(GetSourceFile(config.mirror)).read())
        repos = actions.migrate_repositories(source, mirror, repos, {
            "mirror": True,
            "private": config.private,
            "wiki": config.wiki
        })

    if config.destination is None and config.mirror is None:
        logging.error("should specify at least a destination or a mirror for the migration to happen")

def do_delete(config):
    target = actions.read_profile(File.absolute(GetSourceFile(config.source)).read())
    local_db = DB.new(config.update_db)

    if config.target:
        repos = [Repository.from_html_url(config.target)]
    else:
        repos = (local_db.platform(target['platform'])
                         .user(target['user'])
                         .credentials(target['credentials'])
                         .get_repositories())
    
    actions.delete_repositories(target, repos)
    (local_db.clear()
             .platform(target['platform'])
             .user(target['user'])
             .set_repositories([]))

def main_cli():
    config = Cli.run()
    
    if config.verb == 'list':
        do_list(config)
    elif config.verb == 'migrate':
        do_migrate(config)
    elif config.verb == 'delete':
        do_delete(config)

if __name__ == "__main__":
    main_cli()
