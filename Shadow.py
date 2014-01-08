import sqlite3


class Shadow(object):
    def __init__(self, key_pass):
        self._key_pass = key_pass
        self._conn = sqlite3.connect("secret.db")

        # This allows us to access rows by thier name
        self._conn.row_factory = sqlite3.Row
        # And ensure we are using ASCII representation, no need for UTF here
        self._conn.text_factory = str

        # Cache availiable sets internally
        self._setCache = {}
        self._setCacheIsValid = False

        try:
            self.initDb()
        except Exception:
            print 'Something has gone wrong initializing the database'
            quit()

    def initDb(self):
        c = self._conn.cursor()
        #desencrypt database
        database_key = 'PRAGMA key=' + self._key_pass
        c.execute(database_key)
        with open('db.sql', 'r') as f:
            buildUpQuery = f.read()
        # Create tables if they don't already exist
        c.executescript(buildUpQuery)

    def importDb(self, db):
        c = self._conn.cursor()
        #desencrypt database
        database_key = 'PRAGMA key=' + self._key_pass
        c.execute(database_key)
        with open(db, 'r') as f:
            buildUpQuery = f.read()
        # Create tables if they don't already exist
        c.executescript(buildUpQuery)

    def getInfo(self):
        if not self._setCacheIsValid:
            c = self._conn.cursor()
            c.execute("SELECT * FROM information")

        return c.fetchall()

    def searchInfo(self, value):
        if not self._setCacheIsValid:
            c = self._conn.cursor()
            query = "SELECT * FROM information where name like '%" + value + "%'"
            c.execute(query)
        return c.fetchall()

    def addInfo(self, setName, setUser, setPass):
        c = self._conn.cursor()
        c.execute('INSERT INTO information (name,user,password) VALUES (?,?,?)', (setName, setUser, setPass,))
        newSetId = c.lastrowid
        self._conn.commit()

        return newSetId

    def delInfo(self, setO):
        with self._conn as c:
            c.execute('DELETE FROM information WHERE id = ?', (setO._sid, ))
        del self._setCache[setO._sid]
