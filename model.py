import sqlite3 as sql
from flask_sqlalchemy import SQLAlchemy


# Class to create CRUD in our api
class Connection_db:
    # Creating the connection and the db according to the schema
    def create_conn(self):
        try:
            conn = sql.connect('coink.db')

            with open('database/schema.sql') as file:
                conn.executescript(file.read())
            return conn
        except Exception as e:
            msg_error = f'Error en la conexión: {e}'
            return msg_error

    # Method to add users to the table "users"
    def add_records(self, name, email, city):
        try:
            conn = self.create_conn()
            cursor = conn.cursor()
            sql_query = f'INSERT INTO users (user_full_name, user_email, user_city) ' \
                        f'VALUES ("{name}", "{email}", "{city}")'
            cursor.execute(sql_query)
            conn.commit()
            conn.close()
        except Exception as e:
            msg_error = f'Error al intentar guardar el registro: {e}'
            return msg_error

    # Method to show our data into the database:
    def show_users(self):
        conn = self.create_conn()
        cursor = conn.cursor()
        sql_query = 'SELECT * FROM users'
        records = cursor.execute(sql_query)
        records = records.fetchall()
        conn.close()
        return records
