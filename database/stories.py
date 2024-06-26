from base.db_connection import DatabaseOperations


class StoriesDB(DatabaseOperations):

    def find_story_by_id(self, story_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT * FROM stories WHERE id={story_id};")
        result = db_cursor.fetchone()
        db.close()
        return result

    def get_story_views(self, story_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT views FROM stories WHERE id={story_id}")
        result = db_cursor.fetchone()[0]
        db.close()
        return result
