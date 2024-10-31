import sqlite3
from typing import List
from sqlalchemy import Sequence, create_engine
from sqlalchemy import select
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from db.models import Post, Base


class Database:
    def __init__(self, db_name: str = "db.sqlite3"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.engine: Engine = create_engine("sqlite:///db.sqlite3")

    def get_posts(self) -> Sequence[Post]:
        select_stmt = select(Post)

        return Session(self.engine).scalars(select_stmt).all()

    def create_tables(self):
        Base.metadata.create_all(self.engine)
        self.conn.commit()

    def insert(self, row: Base | List[Base]):
        with Session(self.engine) as session:
            if isinstance(row, list):
                session.add_all(row)
            else:
                session.add(row)
            session.commit()

    # Just for debugging # TODO: Remove when ready
    def populate_table(self, post: Base):
        self.engine.insert(post)
        self.conn.commit()

    def drop(self, table: Base):
        Base.metadata.drop_all(self.engine)


if __name__ == "__main__":
    # Just for debugging # TODO: Replace with proper tests
    db = Database()
    db.create_tables()
    five_posts = [
        Post("John Doe", "First Post", "This is the first post", "April 20, 2018"),
        Post("Jane Doe", "Second Post", "This is the second post", "April 21, 2018"),
        Post("John Doe", "Third Post", "This is the third post", "April 22, 2018"),
        Post("Jane Doe", "Fourth Post", "This is the fourth post", "April 23, 2018"),
        Post("John Doe", "Fifth Post", "This is the fifth post", "April 24, 2018"),
    ]
    db.insert(five_posts)
    res = db.get_posts()
    from pprint import pprint
    pprint(res)
    db.drop(Post)
