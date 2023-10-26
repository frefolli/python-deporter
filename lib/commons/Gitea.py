from __future__ import annotations
import lib.utils as utils

import lib.commons.Platform as Platform
import lib.commons.Credentials as Credentials
import lib.commons.Repository as Repository
import lib.commons.User as User

import requests
import logging

class Gitea(Platform):
    @staticmethod
    @utils.deprecated("Use Platform.from_dict instead")
    def from_env(key: str) -> Gitea:
        import lib.secrets as secrets
        return Gitea(secrets.get_env_or_raise("%s_GITEA_URL" % key))

    def __init__(self, instance: str):
        super().__init__(instance)

    def get_user_repositores(self, user: User, credentials: Credentials) -> list[Repository]:
        auth = (credentials.get_username(),
                credentials.get_token())
        headers = {
            "accept": "application/json"
        }
        username = user.get_username()
        response = requests.get("%s/api/v1/users/%s/repos" % (self.get_url(),
                                                              username),
                                headers=headers, auth=auth)
        return [Repository.from_dict(_) for _ in response.json()]

    def _validate_migration_config(self, config: dict = None) -> dict:
        if config is None:
            config = {}
        if "mirror" not in config:
            config["mirror"] = False
        if "private" not in config:
            config["private"] = False
        if "wiki" not in config:
            config["wiki"] = True
        return config

    def migrate_repository(self, repo: Repository, config: dict, credentials: Credentials) -> Repository:
        config = self._validate_migration_config(config)
        url = "%s/api/v1/repos/migrate" % self.get_url()
        auth = (credentials.get_username(),
                credentials.get_token())
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        data = {
            "auth_username": credentials.get_username(),
            "auth_token": credentials.get_token(),
            "clone_addr": repo.get_url(),
            "mirror": config["mirror"],
            "private": config["private"],
            "repo_name": repo.get_name(),
            "repo_owner": credentials.get_username(),
            "service": "git",
            "uid": 0,
            "wiki": config["wiki"]
        }
        response = requests.post(url, headers=headers, auth=auth, json=data)
        if bool(response):
            return Repository.from_dict(response.json())
        else:
            logging.error("%s: %s" % (response, response.json()))
            return None
