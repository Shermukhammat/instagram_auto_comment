import sqlite3



class CommentAnswer:
    def __init__(self, id : str, media_id : str, code : str, url : str) -> None:
        self.id = id
        self.media_id = media_id
        self.code = code
        self.url = url

class CommentAnswersData:
    def __init__(self, path : str) -> None:
        self.path = path
        self.comment_answers_cache : dict[CommentAnswer] = {}

    def add_comment_data(self, data : CommentAnswer):
        con = sqlite3.connect(self.path)
        cursor = con.cursor()

        cursor.execute("INSERT INTO comment_answers (id, media_id, code, url) VALUES(?,?,?,?);", (data.id, data.media_id, data.code, data.url))
        self.comment_answers_cache[data.id] = data

        con.commit()
        con.close()

    def get_comment_data(self, id : str) -> CommentAnswer:
        if self.comment_answers_cache.get(id):
            return self.comment_answers_cache[id]
        
        con = sqlite3.connect(self.path)
        cursor = con.cursor()

        answer = None
        for row in cursor.execute("SELECT * FROM comment_answers WHERE id == ?", (id,)):
            answer = CommentAnswer(row[0], row[1], row[2], row[3])
            self.comment_answers_cache[id] = answer

        con.close()
        return answer
    
    def delet_commit_data(self, id : str):
        if self.comment_answers_cache.get(id):
            del self.comment_answers_cache[id]

        con = sqlite3.connect(self.path)
        cursor = con.cursor()

        cursor.execute("DELETE FROM comment_answers WHERE id == ?;", (id,))

        con.commit()
        con.close()
    


    