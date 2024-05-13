from base.db_connection import get_social_db


class StoriesDB:
    def __init__(self):
        self.db_cursor = get_social_db.cursor(buffered=True)

    def find_story_by_id(self, story_id):
        self.db_cursor.execute(f"SELECT * FROM stories WHERE id={story_id};")
        return self.db_cursor.fetchone()

    def get_story_views(self, story_id):
        self.db_cursor.execute(f"SELECT views FROM stories WHERE id={story_id}")
        return self.db_cursor.fetchone()[0]
