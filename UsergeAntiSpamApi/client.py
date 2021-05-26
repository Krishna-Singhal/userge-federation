import requests
from json import JSONDecodeError
from typing import Union, List

from .errors import *
from .types import *


class Client(object):
    ''' Api Wrapper '''

    def __init__(self, token: str) -> None:
        self.token = token
        response = requests.get(
            f"https://api.userge.tk/checktoken?api_key={self.token}"
        )
        if response.status_code != 201:
            self._raise_error(response)
    
    def get_version(self) -> str:
        response = requests.get("https://api.userge.tk/version")
        if response.status_code == 201:
            return response.json()["version"]
        else:
            self._raise_error(response)
    
    def get_api_stats(self) -> int:
        response = requests.get("https://api.userge.tk/stats")
        if response.status_code == 201:
            return int(response.json()["number_of_bans"])
        else:
            self._raise_error(response)
    
    def getban(self, user_id: int) -> Union[Ban, bool]:
        response = requests.get(f"https://api.userge.tk/ban?api_key={self.token}&user_id={user_id}")
        if response.status_code == 201:
            if response.json()["success"]:
                return Ban(**response.json())
            else:
                return False
        else:
            self._raise_error(response)
    
    def getbans(self) -> Union[List[Ban], bool]:
        response = requests.get("https://api.userge.tk/ban")
        if response.status_code == 201:
            if response.json()["success"]:
                return [Ban(**data) for data in response.json()["users"]]
        else:
            self._raise_error(response)

    def add_ban(self, user_id: int, reason: str) -> bool:
        data = {
            "api_key": self.token,
            "user_id": user_id,
            "reason": reason
        }

        response = requests.post("https://api.userge.tk/ban", data=data)
        if response.status_code == 201:
            return True
        else:
            self._raise_error(response)
    
    def update_ban(self, user_id: int, reason: str) -> bool:
        data = {
            "api_key": self.token,
            "user_id": user_id,
            "reason": reason
        }

        response = requests.post("https://api.userge.tk/updateban", data=data).json()
        if response.status_code == 201:
            return True
        else:
            self._raise_error(response)

    def delete_ban(self, user_id: int) -> bool:
        data = {
            "api_key": self.token,
            "user_id": user_id
        }

        response = requests.delete("https://api.userge.tk/ban", data=data)
        if response.status_code == 201:
            return True
        else:
            self._raise_error(response)
    
    def get_me(self) -> Token:
        data = {"api_key": self.token}
        response = requests.get("https://api.userge.tk/token/self", data=data)
        if response.status_code == 201:
            return Token(**response.json())
        else:
            self._raise_error(response)
    
    def promote_user(self, user_id: int, permssions: list) -> bool:
        perms = ""
        for i in permssions:
            perms += i + " "
        perms = perms.strip()
        data = {
            "api_key": self.token,
            "user_id": user_id,
            "perms": perms
        }
        response = requests.post("https://api.userge.tk/promotetoken", data=data)
        if response.status_code == 201:
            return True
        else:
            self._raise_error(response)
    
    def demote_user(self, user_id: int) -> bool:
        data = {
            "api_key": self.token,
            "user_id": user_id
        }
        response = requests.post("https://api.userge.tk/demotetoken", data=data)
        if response.status_code == 201:
            return True
        else:
            self._raise_error(response)
    
    def delete_my_token(self) -> bool:
        data = {
            "api_key": self.token
        }
        response = requests.delete("https://api.userge.tk/token", data=data)
        if response.status_code == 201:
            return True
        else:
            self._raise_error(response)

    def _raise_error(self, response):
        try:
            message = response.json()["message"]
        except JSONDecodeError:
            raise InternalServerError("Server having some internal Problems, please try again later")
        if response.status_code == 401:
            raise Unauthorised(message)
        elif response.status_code == 403:
            raise Forbidden(message)
        elif response.status_code == 404:
            raise NotFoundError(message)
        else:
            raise BadRequest(message)
