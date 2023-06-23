import cloudscraper
from .chat import Chat
from .user import User
from .auth import Auth
from .helper import KICK_BASE_URL, KICK_API_BASE_URL_V1

class KickAPI:
    def __init__(self, debug=False):
        scraper = cloudscraper.CloudScraper(debug=debug)
        self.chat = Chat(scraper)
        self.user = User(scraper)
        self.auth = Auth(scraper)
        self.__initialize(scraper)

    def __initialize(self, scraper):
        scraper.get(KICK_BASE_URL) # Kick.com must be accessed first to set initial session cookies