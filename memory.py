import sqlite3

def createTable():
    db = sqlite3.connect("memory.db")
    c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS dialog(
        me text,
        shiro text
    )""")
    db.commit()
    db.close()

def readeTable():
    db = sqlite3.connect("memory.db")
    c = db.cursor()

    c.execute("SELECT * FROM dialog")
    print(c.fetchall())
    db.close()

def updateTable(user_say, response):
    db = sqlite3.connect("memory.db")
    c = db.cursor()

    c.execute("INSERT INTO dialog VALUES (?,?)", (user_say, response))
    db.commit()
    db.close()

def deleteTable():
    db = sqlite3.connect("memory.db")
    c = db.cursor()

    c.execute("DELETE FROM dialog WHERE rowid = (SELECT MAX(rowid) FROM dialog)")
    db.commit()
    db.close()