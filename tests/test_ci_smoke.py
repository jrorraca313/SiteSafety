"""Placeholder tests so CI has something to run before the real code lands.
Delete them once each part has its own tests."""

import pytest


def test_unit_job_runs():
    assert 1 + 1 == 2


@pytest.mark.integration
def test_database_is_reachable(db_conn):
    assert db_conn.execute("SELECT 1").fetchone() == (1,)
