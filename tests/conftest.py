import os
import pytest

# Выставляем TESTING до импорта app, чтобы config.py выбрал SQLite
os.environ.setdefault("TESTING", "1")

from app import app, db

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        with app.app_context():
            db.create_all()
            yield c
            db.session.remove()
            db.drop_all()
