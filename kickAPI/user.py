from .helper import KICK_API_BASE_URL_V2

class User:
    def __init__(
            self,
            scraper,
            user_id = None,
            slug = None,
            account_id = None
    ):
        self.scraper = scraper
        self.account_id = account_id
        self.user_id = user_id
        self.slug = slug
        

    def get_user(self, username: str):
        '''
        :param str username: username that is seen in the url of the profile
        '''
        url = KICK_API_BASE_URL_V2 + "/channels/" + username
        r = self.scraper.get(url).json()
        return User(self.scraper, user_id=r["user_id"], slug=r["slug"], account_id=r["id"])