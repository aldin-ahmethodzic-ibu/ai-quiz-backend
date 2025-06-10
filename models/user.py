from beanie import Document, Indexed
from pydantic import EmailStr, Field
from datetime import datetime, timezone

class User(Document):
    user_id: int = Indexed(int, unique=True)
    email: EmailStr = Indexed(EmailStr, unique=True)
    username: str
    hashed_password: str
    joined_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "users"