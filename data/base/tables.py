import sqlite3



def creat_tables(path : str):
    con = sqlite3.connect(path)
    cursor = con.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS comment_answers(id TEXT UNIQUE, media_id TEXT, code TEXT, url TEXT);")

    con.commit()
    con.close()