import pytest
from src.processing import filter_by_state, sort_by_date
@pytest.fixture
def get_test_state():
    return [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},]

def test_filter_by_state(get_test_state):
    result = filter_by_state(get_test_state)
    assert len(result) == 2
    assert result[0]["id"] == 41428829
    assert result[1]["id"] == 939719570

def test_filter_by_state_canceled(get_test_state):
    result = filter_by_state(get_test_state, key="CANCELED")
    assert len(result) == 1
    assert result[0]["id"] == 594226727

def test_filter_by_state_empty(get_test_state):
    assert filter_by_state([], "EXECUTED") == []


@pytest.fixture
def sample_data():
    return [
        {"date": "2019-10-10", "id": 1},
        {"date": "2023-01-01", "id": 2},
        {"date": "2021-05-20", "id": 3}
    ]
def test_sort_by_date_descending(sample_data):
    result = sort_by_date(sample_data, reverse=True)
    assert result[0]["date"] > result[-1]["date"]
    assert result[0]["id"] == 2

def test_sort_by_date_ascending(sample_data):
    result = sort_by_date(sample_data, reverse=False)
    assert result[0]["date"] < result[-1]["date"]
    assert result[0]["id"] == 1

def test_sort_by_date_empty(sample_data):
    assert sort_by_date([]) == []