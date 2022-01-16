import sqlite3 as sql


# Class to create CRUD in our api
class Connection_db:
    # Main path to create the DB
    DB_PATH = '/home/Documents/database/coink.db'

    #
    def crearte_conn(self):
        conn = sql.connect(self.DB_PATH)
        return conn

    def create_cursor(self):
        conn = sql.connect(self.DB_PATH)
        cursor = conn.cursor()
        return cursor

    def create_DB(self):
        # We build a connection to create our tables
        conn = self.crearte_conn()
        cursor = self.create_cursor()
        cursor.execute("""CREATE TABLE users(
            user_full_name text,
            user_email text,
            user_city text)
        """)
        conn.commit()
        conn.close()

    def add_records(self):
        pass