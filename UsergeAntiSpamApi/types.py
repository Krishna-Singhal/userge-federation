from typing import Dict, List, Union
from datetime import datetime


class Admin():
    user_id: int
    name: str

    def parse(user_id: int, name: str, **kwargs) -> None:
        self.user_id = user_id
        self.name = name

class Token():
    token: str
    user_id: int
    name: str
    type: str
    permissions: List[str]

    def parse(token: str, user_id: int, name:str, type:str, permissions: List[str], **kwargs) -> None:
        self.token = token
        self.user_id = user_id
        self.name = name
        self.type = type
        self.permissions = permissions


class Ban():
    user_id: int
    reason: str
    date: int
    admin: Admin

    def parse(user_id: int, reason: str, date: int, banned_by: Dict[str, Union[int, str]], **kwargs) -> None:
        self.user_id = user_id
        self.reason = reason
        self.date = datetime.fromtimestamp(date)
        self.admin = Admin.parse(banned_by)