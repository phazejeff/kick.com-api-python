from typing import List
from .helper import KICK_API_BASE_URL_V2
from dateutil import parser
from .user import User

class Message:
    def __init__(
            self,
            id,
            chat_id,
            user_id,
            content,
            type,
            metadata,
            created_at,
            sender
    ):
        self.id = id
        self.chat_id = chat_id
        self.user_id = user_id
        self.content = content
        self.type = type
        self.metadata = metadata
        self.created_at = parser.parse(created_at)
        self.sender = User(sender["id"], sender["slug"])

class Chat:
    def __init__(self, scraper):
        self.scraper = scraper

    def get_chat(self, account_id: int) -> List[Message]:
        '''
        Returns last 50 messages in chat
        '''
        url = KICK_API_BASE_URL_V2 + "/channels/" + str(account_id) + "/messages"
        r = self.scraper.get(url).json()
        
        messages = []
        for m in r["data"]["messages"]:
            messages.append(Message(**m))
        return messages
