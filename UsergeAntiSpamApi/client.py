import requests
from .errors import InvalidApiToken


class Client(object):

    def __init__(self, token: str = None):
        self.token = token
        response = requests.get(
            f"https://api.userge.tk/checktoken?api_key={self.token}"
        ).status_code
        if response != 201:
            raise InvalidApiToken("Your Api Token is invalid")
    
    def get_version(self):
        return requests.get("https://api.userge.tk/version")
    
    def get_api_stats(self):
        return requests.get("https://api.userge.tk")
    
    def getban(self, user_id: int):
        return requests.get("https://api.userge.tk/ban?user_id={}".format(user_id)).json()
    
    def getbans(self):
        return requests.get("https://api.userge.tk/ban")

    def add_ban(self, user_id: int, reason: str):
        data = {
            "api_key": self.token,
            "user_id": user_id,
            "reason": reason
        }

        return requests.post("https://api.userge.tk/ban", data=data).json()
    
    def update_ban(self, user_id: int, reason: str):
        data = {
            "api_key": self.token,
            "user_id": user_id,
            "reason": reason
        }

        return requests.post("https://api.userge.tk/updateban", data=data).json()

    def delete_ban(self, user_id: int):
        data = {
            "api_key": self.token,
            "user_id": user_id
        }

        return requests.delete("https://api.userge.tk/ban", data=data)
    
    def get_me(self):
        data = {"api_key": self.token}
        return requests.get("https://api.userge.tk/token/self", data=data)
    
    def promote_user(self, user_id: int, permssions: list):
        perms = ""
        for i in permssions:
            perms += i + " "
        perms = perms.strip()
        data = {
            "api_key": self.token,
            "user_id": user_id,
            "perms": perms
        }
        return requests.post("https://api.userge.tk/promotetoken", data=data)
    
    def demote_user(self, user_id: int):
        data = {
            "api_key": self.token,
            "user_id": user_id
        }
        return requests.post("https://api.userge.tk/demotetoken", data=data)
    
    def delete_my_token(self):
        data = {
            "api_key": self.token
        }
        return requests.delete("https://api.userge.tk/token", data=data)
