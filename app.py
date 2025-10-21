from flask import Flask, jsonify, request
import sqlite3
from utils.http_client import fetch_json
from utils.service_layer import search_users_chain
from utils.models import EchoPayload
from utils import secret_fixtures  # imported so scanners see Python secrets

app = Flask(__name__)


@app.get("/")
def root():
    return jsonify({"ok": True, "service": "python-pip-demo"})


@app.get("/echo")
def echo():
    msg = request.args.get("msg", "hello")
    return jsonify({"echo": msg})


@app.get("/httpbin")
def httpbin():
    data = fetch_json("https://httpbin.org/get")
    return jsonify({"httpbin": data})


@app.post("/validate")
def validate():
    payload = request.get_json(silent=True) or {}
    try:
        model = EchoPayload(**payload)
    except Exception as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400
    return jsonify({"ok": True, "data": model.model_dump()})


@app.get("/users/search-single")
def search_single_file():
    # Vulnerable single-file SQL injection for scanner testing (unsanitized input in query)
    term = request.args.get("q", "")
    conn = sqlite3.connect(":memory:")
    try:
        cur = conn.cursor()
        cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)")
        cur.execute("INSERT INTO users(name) VALUES ('alice'),('bob'),('carol')")
        # INTENTIONAL VULNERABILITY: string concatenation into SQL
        sql = "SELECT id, name FROM users WHERE name LIKE '%" + term + "%'"
        rows = cur.execute(sql).fetchall()
        return jsonify({"results": rows})
    finally:
        conn.close()


@app.get("/users/search-chain")
def search_chain():
    # Cross-file vulnerable route: flows through service -> repo -> SQL concat
    term = request.args.get("q", "")
    rows = search_users_chain(term)
    return jsonify({"results": rows})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
