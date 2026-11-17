import os

import pytest


@pytest.fixture
def db_conn():
    """A connection to the test database. Integration tests only.

    CI sets DATABASE_URL. Locally, point it at your own PostgreSQL to run these,
    or leave it unset and they are skipped.
    """
    url = os.environ.get("DATABASE_URL")
    if not url:
        pytest.skip("DATABASE_URL not set")
    import psycopg

    with psycopg.connect(url) as conn:
        yield conn
        conn.rollback()  # nothing a test writes is kept
