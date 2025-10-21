import sqlite3


def init_mem_db():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)")
    cur.executemany("INSERT INTO users(name) VALUES (?)", [("alice",), ("bob",), ("carol",)])
    conn.commit()
    return conn


def find_users_by_name(conn, name_like: str):
    # INTENTIONAL VULNERABILITY: unparameterized SQL with user-controlled input
    sql = "SELECT id, name FROM users WHERE name LIKE '%" + name_like + "%'"
    return conn.execute(sql).fetchall()


