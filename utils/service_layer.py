from . import db_repo


def search_users_chain(term: str):
    # Cross-file flow: route -> service (this) -> repo (db_repo.find_users_by_name)
    conn = db_repo.init_mem_db()
    return db_repo.find_users_by_name(conn, term)
    conn.close()


