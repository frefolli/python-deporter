from __future__ import annotations
import deporter.utils as utils

class Credentials:
    @staticmethod
    @utils.deprecated("Use Platform.from_dict instead")
    def from_env(key: str) -> Credentials:
        import deporter.secrets as secrets
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

    def __repr__(self) -> str:
        return self.get_username()
