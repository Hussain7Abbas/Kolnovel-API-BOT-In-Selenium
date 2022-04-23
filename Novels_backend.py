import sqlite3
from sqlite3 import Error

database = "novels.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def setupDB():
    conn = create_connection(database)
    cur = conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS novels (
    name VARCHAR(32),
    chapter INTEGER,
    body TEXT NOT NULL,
    PRIMARY KEY (name, chapter)
);'''
    cur.execute(sql)
    conn.commit()

setupDB()

def getChapter(name:str, chapter:int):
    conn = create_connection(database)
    cur = conn.cursor()
    sql = '''SELECT * FROM novels WHERE name="%s" AND chapter=%s''' %(name, chapter)
    cur.execute(sql)
    return cur.fetchone()[2]

def getNovelsNames():
    conn = create_connection(database)
    cur = conn.cursor()
    sql = '''SELECT DISTINCT name FROM novels GROUP BY name'''
    cur.execute(sql)
    names = []
    for name in cur.fetchall():
        names.append(name[0])
    return names

def getNovelChapters(name:str):
    conn = create_connection(database)
    cur = conn.cursor()
    sql = '''SELECT chapter FROM novels WHERE name="%s"''' %(name)
    cur.execute(sql)
    names = []
    for name in cur.fetchall():
        names.append(name[0])
    return names

def saveNovel(name:str, chapter:int, text):
    conn = create_connection(database)
    cur = conn.cursor()
    sql = '''
        INSERT INTO novels(name,chapter,body) VALUES("%s",%s,"%s");
    ''' % (name, chapter, text)
    cur.execute(sql)
    conn.commit()


def deleteChapter(name:str, chapter:int):
    conn = create_connection(database)
    cur = conn.cursor()
    sql = ''' DELETE FROM novels WHERE name = '%s' AND chapter = %s;
    ''' % (name, chapter)
    cur.execute(sql)
    conn.commit()

def clearNovel(name:str):
    conn = create_connection(database)
    cur = conn.cursor()
    sql = ''' DELETE FROM novels WHERE name = '%s';
    ''' % (name)
    cur.execute(sql)
    conn.commit()
