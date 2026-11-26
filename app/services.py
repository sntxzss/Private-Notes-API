from app.security import hash_password, verify_password
from app.storage import USERS, new_id

class NotFound(Exception):
    def __init__(self, message: str = "Not found"):
        self.message = message
        super().__init__(message)

class Conflict(Exception):
    def __init__(self, message: str = "Conflict"):
        self.message = message
        super().__init__(message)


def get_user_by_email(email: str) -> dict | None:
    for user in USERS.values():
        if user["email"] == email:
            return user
    return None

