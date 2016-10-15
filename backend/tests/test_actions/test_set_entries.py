
import pytest
from voting.actions import set_entries


@pytest.fixture
def entries():
    return ['Trainspotting', '28 Days Later']


@pytest.fixture
def state():
    return {}


def test_set_entries(state, entries):
    next_state = set_entries(state, entries)
    assert next_state == {'entries': tuple(entries)}


def test_set_entries_is_immutable(state, entries):
    next_state = set_entries(state, entries)
    assert state != next_state
    assert state == {}
    assert id(state) != id(next_state)


def test_set_entries_entries_is_tuple(state, entries):
    next_state = set_entries(state, entries)
    assert isinstance(next_state['entries'], tuple)
