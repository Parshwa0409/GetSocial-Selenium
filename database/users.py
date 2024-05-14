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
