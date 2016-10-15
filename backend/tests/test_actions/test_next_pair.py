
import pytest
from voting.actions import next_pair


@pytest.fixture
def state():
    return {
        'entries': ['Trainspotting', '28 Days Later', 'Sunshine'],
    }


@pytest.fixture
def state_with_tally_and_pair():
    return {
        'vote': {
            'pair': ('Trainspotting', '28 Days Later'),
            'tally': {
                'Trainspotting': 4,
                '28 Days Later': 2
            },
        },
        'entries': ('Sunshine', 'Millions', '127 Hours')
    }


def test_next_pair(state):
    next_state = next_pair(state)
    assert next_state['vote']['pair'] == ('Trainspotting', '28 Days Later')
    assert next_state['entries'] == ('Sunshine',)


def test_next_pair_is_immutable(state):
    next_state = next_pair(state)
    assert next_state != state
    assert id(next_state) != id(state)


def test_next_pair_when_entries_is_a_tuple(state):
    state['entries'] = tuple(state['entries'])
    next_state = next_pair(state)
    assert next_state['vote']['pair'] == ('Trainspotting', '28 Days Later')
    assert next_state['entries'] == ('Sunshine',)


def test_should_put_winner_back_to_entries(state_with_tally_and_pair):
    state = state_with_tally_and_pair
    next_state = next_pair(state)
    assert next_state['vote']['pair'] == ('Sunshine', 'Millions')
    assert 'Trainspotting' in next_state['entries']
    assert '28 Days Later' not in next_state['entries']
    assert 'tally' not in next_state


def test_should_put_winner_back_to_entries_1(state_with_tally_and_pair):
    state = state_with_tally_and_pair
    state['vote']['pair'] = reversed(state['vote']['pair'])
    next_state = next_pair(state)
    assert next_state['vote']['pair'] == ('Sunshine', 'Millions')


def test_should_put_all_back_when_tie(state_with_tally_and_pair):
    state = state_with_tally_and_pair
    state['vote']['tally'] = {'Trainspotting': 3, '28 Days Later': 3}
    next_state = next_pair(state)
    next_state['vote']['pair'] = ('Sunshine', 'Millions')
    assert 'Trainspotting' in next_state['entries']
    assert '28 Days Later' in next_state['entries']
    assert 'tally' not in next_state


def test_marks_winner_when_just_one_entry_left(state_with_tally_and_pair):
    state = state_with_tally_and_pair
    state['entries'] = ()
    next_state = next_pair(state)
    assert next_state['winner'] == 'Trainspotting'

    state = state_with_tally_and_pair
    state['vote']['pair'] = reversed(state['vote']['pair'])
    state['entries'] = ()
    next_state = next_pair(state)
    assert next_state['winner'] == 'Trainspotting'


def test_when_there_is_no_entries_and_have_draw(state_with_tally_and_pair):
    state = state_with_tally_and_pair
    state['entries'] = ()
    state['vote']['tally'] = {'Trainspotting': 3, '28 Days Later': 3}
    next_state = next_pair(state)
    assert next_state['vote']['pair'] == state['vote']['pair']
