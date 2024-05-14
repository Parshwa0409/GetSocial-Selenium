import mysql.connector

class DatabaseOperations:
    def __init__(self):
        pass

    def connect_to_db(self):
        get_social_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MYSQLpassword0409!",
            database='get_social_dev'
        )

        return get_social_db
