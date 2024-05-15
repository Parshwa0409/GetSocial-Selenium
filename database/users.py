from base.db_connection import DatabaseOperations


class UsersDB(DatabaseOperations):
    def find_user_by_id(self, user_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT * FROM users WHERE id={user_id};")
        result = db_cursor.fetchone()
        db.close()
        return result

    def find_user_email_by_id(self, user_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT email FROM users WHERE id={user_id};")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def find_count_of_users_with_like_name(self, name):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT COUNT(*) FROM users WHERE name LIKE '%{name}%'")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def find_count_of_users_with_email(self, email):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT COUNT(*) FROM users WHERE email LIKE '%{email}%'")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def find_name_of_user_by_email(self, email):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT name FROM users WHERE email='{email}'")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

# udb = UsersDB()
# udb.find_count_of_users_with_like_name("parshwa")
