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

# class Auth:
#     def __init__(self, auth_param_name, auth_token, kick_session, xsrf_token):
#         self.auth_param_name = auth_param_name
#         self.auth_token = auth_token
#         self.kick_session = kick_session
#         self.xsrf_token = xsrf_token
    
#     def get_cookies(self):
#         return {
#             "kick_session" : self.kick_session,
#             "XSRF-TOKEN": self.xsrf_token,
#             self.auth_param_name : self.auth_token
#         }
    
#     def set_bearer(self, bearer):
#         self.bearer = "Bearer " + bearer

# def get_session():
#     r = scraper.get(KICK_BASE_URL, headers={"content-type": "text/html; charset=UTF-8"})
#     cookies: List[Tuple(str, str)] = r.cookies.items()
#     for c in r.cookies.items():
#         if c[0] == "__cf_bm":
#             cookies.remove(c)
#         elif c[0] == "kick_session":
#             kick_session = c[1].replace("%3D", "=")
#             cookies.remove(c)
#         elif c[0] == "XSRF-TOKEN":
#             xsrf_token = c[1].replace("%3D", "=")
#             cookies.remove(c)
#     auth_param_name = cookies[0][0]
#     auth_token = cookies[0][1].replace("%3D", "=") # by process of elimination, the last thing must be the auth token

#     return Auth(auth_param_name, auth_token, kick_session, xsrf_token)

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
