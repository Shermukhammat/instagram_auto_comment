import sqlite3


class PhotoData:
    def __init__(self, path : str) -> None:
        self.path = path

        con = sqlite3.connect(path)
        cursor = con.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS images(image TEXT UNIQUE);")
        
        con.commit()
        con.close()

        self.data = []

    

    def is_file_exsist(self, file_name : str) -> bool:
        if file_name in self.data:
            return True
        
        con = sqlite3.connect(self.path)
        cursor = con.cursor()

        for row in cursor.execute("SELECT image FROM images WHERE image == ?;", (file_name,)):
            con.commit()
            con.close()

            self.data.append(row[0])
            return True
        
        con.commit()
        con.close()

        return False
    

    def add_file(self, file_name : str) -> bool:
        con = sqlite3.connect(self.path)
        cursor = con.cursor()

        cursor.execute("INSERT INTO images (image) VALUES(?);", (file_name,))

        con.commit()
        con.close()

        return True
    
    def delet_file(self, file_name : str):
        con = sqlite3.connect(self.path)
        cursor = con.cursor()

        cursor.execute("""DELETE FROM images WHERE image == ?;""", (file_name,))

        con.commit()
        con.close()

        if file_name in self.data:
            del self.data[file_name]

    def clear_cache(self):
        self.data.clear()
    
    
    
if __name__ == '__main__':
    db = PhotoData('test.db')
    print(db.is_file_exsist('balj.jpg'))
    # print(db.add_file('balj.jpg'))