from flask import Flask, jsonify, request
from utils.http_client import fetch_json
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
