import lib.commons.Credentials as Credentials

class User:
    def __init__(self,
                 username: str):
        self._username = username

    def get_username(self) -> str:
        return self._username

    def authenticate(self, token: str) -> Credentials:
        return Credentials(self._username, token)

    def __repr__(self) -> str:
        return self.get_username()
