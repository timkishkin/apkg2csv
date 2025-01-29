import sqlite3
import json 

class DBConnect:

    def connect(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Exception as e:
            print(e)
        return conn

    def header(conn):
        cur = conn.cursor()
        cur.execute("SELECT models FROM col")
        rows = cur.fetchall()
        
        items = json.loads(rows[0][0])
        items = items.pop(list(items)[0])
        
        fields = [_['name'] for _ in items['flds']]
        return [*fields, 'tags']

    def values(conn):
        cur = conn.cursor()
        cur.execute("SELECT flds,tags FROM notes")
        rows = cur.fetchall()
        
        return [[*_[0].split("\x1f"), _[1]] for _ in rows]

