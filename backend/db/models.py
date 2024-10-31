import json
from datetime import datetime

from sqlalchemy import String
from sqlalchemy import create_engine

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped

engine = create_engine("sqlite:///db.sqlite3")


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    date_posted: Mapped[datetime] = mapped_column(String)

    def __init__(
            self,
            author: str,
            title: str,
            content: str,
            date_posted: datetime
        ):  # noqa: E125 Flake 8 is being too strict/wrong here

        self.author = author
        self.title = title
        self.content = content
        self.date_posted = date_posted

    def __repr__(self):
        return (
            f"Post(author={self.author}, "
            f"title={self.title}, "
            f"content={self.content}, "
            f"date_posted={self.date_posted})"
        )

    def as_json(self) -> json:
        """Return a JSON representation of the post."""
        return {
            "author": self.author,
            "title": self.title,
            "content": self.content,
            "date_posted": self.date_posted,
        }
