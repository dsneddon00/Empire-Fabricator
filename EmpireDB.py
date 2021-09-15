import sqlite3

#

def dict_factory(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

class EmpireDB:

    def __init__(self):
        self.connection = sqlite3.connect("EmpireDB.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        return

    def getAllFromEmpire(self):
        self.cursor.execute("SELECT * FROM empire")
        data = self.cursor.fetchall()
        return data

    def getOneFromEmpire(self, id):
        data = [id]
        self.cursor.execute("SELECT * FROM empire WHERE id = ?", data)
        result = self.cursor.fetchone()
        return result

    def createLog(self, name):
        data = [name]
        self.cursor.execute("INSERT INTO empire (name) VALUES (?)", data)
        self.connection.commit()
        return

    def updateLog(self, id, name):
        data = [name, id]
        self.cursor.execute("UPDATE empire SET name = ? WHERE id = ?", data)
        self.connection.commit()
        return

    def deleteLog(self, id):
        data = [id]
        self.cursor.execute("DELETE FROM empire SET name = ?", data)
        self.connection.commit()
        return
