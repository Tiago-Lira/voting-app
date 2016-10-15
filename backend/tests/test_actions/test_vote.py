
import pytest
from voting.actions import vote


@pytest.fixture
def state():
    return {
        'pair': ('Trainspotting', '28 Days Later'),
    }


@pytest.fixture
def state_with_tally():
    return {
        'pair': ('Trainspotting', '28 Days Later'),
        'tally': {
            'Trainspotting': 3,
            '28 Days Later': 2
        },
    }


def test_vote(state):
    next_state = vote(state, 'Trainspotting')
    assert next_state['pair'] == ('Trainspotting', '28 Days Later')

    tally = next_state['tally']
    assert list(tally.keys()) == ['Trainspotting']
    assert tally['Trainspotting'] == 1


def test_vote_with_existing_tally(state_with_tally):
    next_state = vote(state_with_tally, 'Trainspotting')
    tally = next_state['tally']
    assert tally['Trainspotting'] == 4
    assert tally['28 Days Later'] == 2


def test_vote_is_immutable(state):
    next_state = vote(state, 'Trainspotting')
    assert id(next_state) != id(state)
    assert next_state != state
