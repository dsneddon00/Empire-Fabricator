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
