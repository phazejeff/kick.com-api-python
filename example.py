from kickAPI import KickAPI

kickAPI = KickAPI()
user = kickAPI.user.get_user("poop-dealer")

messages = kickAPI.chat.get_chat(user.account_id) # gets the past 50 messages sent in chat
print(messages[0].content) # print the first message sent in chat

kickAPI.auth.login("username", "password") # WIP, not working yet.