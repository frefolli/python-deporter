from __future__ import annotations
import lib.secrets as secrets

class Credentials:
    @staticmethod
    def from_env(key: str) -> Credentials:
        username = secrets.get_env_or_raise("%s_USERNAME" % key)
        token = secrets.get_env_or_raise("%s_TOKEN" % key)
        return Credentials(username, token)

    def __init__(self,
                 username: str,
                 token: str):
        self._username = username
        self._token = token

    def get_username(self) -> str:
        return self._username

    def get_token(self) -> str:
        return self._token
