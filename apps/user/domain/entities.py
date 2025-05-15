from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int | None
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def create(cls, username: str, email: str) -> 'User':
        now = datetime.now()
        return cls(
            id=None,
            username=username,
            email=email,
            created_at=now,
            updated_at=now
        )