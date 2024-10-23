import sqlite3
from typing import List, Tuple

class Database:
    def __init__(self, db_name: str = 'db.sqlite3'): 
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
    def get_posts(self) -> List[Tuple[str, str, str, str]]:
        res = self.cursor.execute('''SELECT * FROM posts''')
        
        return res.fetchall()
    
    def create_table(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS posts (author, title, content, date_posted)'''
        )
        self.conn.commit()
    
    # Just for debugging # TODO: Remove when ready
    def populate_table(self):
        self.cursor.execute(
            '''INSERT INTO posts 
               VALUES ('John Doe', 'First Post', 'This is the first post', 'April 20, 2018')'''
        )
        self.cursor.execute(
            '''INSERT INTO posts 
               VALUES ('Jane Doe', 'Second Post', 'This is the second post', 'April 21, 2018')'''
        )
        self.conn.commit()
        
        
        
if __name__ == '__main__':
    db = Database()
    print(db.cursor)