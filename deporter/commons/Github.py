import deporter.commons.Platform as Platform
import deporter.commons.Credentials as Credentials
import deporter.commons.Repository as Repository
import deporter.commons.User as User
import requests
import logging

class Github(Platform):
    def __init__(self):
        super().__init__("https://github.com")

    def get_user_repositores(self, user: User, credentials: Credentials) -> list[Repository]:
        headers = {"Accept": "application/vnd.github.v3+json"}
        auth = (credentials.get_username(),
                credentials.get_token())
        username = user.get_username()
        response = requests.get("https://api.github.com/users/%s/repos" % username,
                                headers=headers,
                                auth=auth)
        logging.warn(response.json())
        return Repository.from_dict_list(response.json())

    def migrate_repository(self, repo: Repository, config: dict, credentials: Credentials) -> Repository:
        raise Exception("repository migration not implemented for `deporter.commons.Github`")

    def delete_repository(self, repo: Repository, credentials: Credentials) -> bool:
        raise Exception("repository deletion not implemented for `deporter.commons.Github`")
