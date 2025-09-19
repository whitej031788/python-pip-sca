# python-pip demo

A minimal Python app for pip/SCA/SonarQube testing.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
FLASK_APP=app.py flask run
# or
python app.py
```

## Test

```bash
pytest -q
```

## Endpoints
- GET `/` health
- GET `/echo?msg=...`
- GET `/httpbin` (uses requests)
- POST `/validate` {"message": str, "count": int}
