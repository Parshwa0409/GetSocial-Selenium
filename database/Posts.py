from base.db_connection import get_social_db


class PostsDB:
    def __init__(self):
        self.db_cursor = get_social_db.cursor(buffered=True)

    def find_post_by_id(self, post_id):
        self.db_cursor.execute(f"SELECT * FROM posts WHERE id={post_id};")
        return self.db_cursor.fetchone()

    def get_post_total_likes(self, post_id):
        self.db_cursor.execute(f"SELECT total_likes FROM posts WHERE id={post_id}")
        return self.db_cursor.fetchone()[0]
