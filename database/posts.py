from base.db_connection import DatabaseOperations


class PostsDB(DatabaseOperations):
    def find_post_by_id(self, post_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT * FROM posts WHERE id={post_id};")
        result = db_cursor.fetchone()
        db.close()
        return result

    def get_post_total_likes(self, post_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT total_likes FROM posts WHERE id={post_id}")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def get_post_total_comments(self, post_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT total_comments FROM posts WHERE id={post_id}")
        result = db_cursor.fetchone()[0]
        db.close()
        return result
