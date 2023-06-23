from .helper import KICK_BASE_URL
from typing import List, Tuple

class TokenProvider:
    def __init__(
            self,
            nameFieldName,
            validFromFieldName,
            encryptedValidFrom
    ):
        self.nameFieldName = nameFieldName
        self.validFromFieldName = validFromFieldName
        self.encryptedValidFrom = encryptedValidFrom

    def get_login_request(self, username: str, password: str):
        return {
            self.nameFieldName : "",
            self.validFromFieldName : self.encryptedValidFrom,
            "email": username,
            "password": password
        }

class Auth:
    def __init__(self, scraper):
        self.scraper = scraper

    def get_token_provider(self) -> TokenProvider:
        url = KICK_BASE_URL + "/kick-token-provider"
        r = self.scraper.get(url).json()

        return TokenProvider(r["nameFieldName"], r["validFromFieldName"], r["encryptedValidFrom"])

    def login(self, username: str, password: str):
        url = KICK_BASE_URL + "/login"
        token_provider = self.get_token_provider()
        # auth = get_session()

        # cookies = auth.get_cookies()
        params = token_provider.get_login_request(username, password)
        # print(scraper.cookies.get_dict())
        # print(cookies)
        r = self.scraper.post(url, data=params)
