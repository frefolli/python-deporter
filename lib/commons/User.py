import lib.commons.Credentials as Credentials

class User:
    def __init__(self,
                 username: str):
        self._username = username
        self._platform = platform

        def get_username(self) -> str:
            return self._username

        def authenticate(self, token: str) -> Credentials:
            return Credentials(self._username, token)
