import lib.commons.Platform as Platform
import lib.commons.Credentials as Credentials
import lib.commons.Repository as Repository
import requests

class Github(Platform):
    def __init__(self):
        super().__init__("https://github.com")

    def get_repositories_of_user(self, user: User, credentials: Credentials) -> list[Repository]:
        headers = {"Accept": "application/vnd.github.v3+json"}
        auth = (credentials.get_username(),
                credentials.get_token())
        username = user.get_username()
        response = requests.get("https://api.github.com/users/%s/repos" % username,
                                headers=headers,
                                auth=auth)
        return [Repository.from_json(_) for _ in response.json()]
