
import functools
from voting.redux import reducer


def test_handle_set_entries():
    initial_state = {}
    action = {'type': 'SET_ENTRIES', 'entries': ['Trainspotting']}
    next_state = reducer(initial_state, action)
    assert next_state['entries'] == ('Trainspotting',)


def test_handle_next_pair():
    initial_state = {'entries': ['Trainspotting', '28 Days Later']}
    action = {'type': 'NEXT'}
    next_state = reducer(initial_state, action)
    assert next_state['vote']['pair'] == ('Trainspotting', '28 Days Later')


def test_handle_vote():
    initial_state = {'vote': {'pair': ('Trainspotting', '28 Days Later')}}
    action = {'type': 'VOTE', 'entry': 'Trainspotting'}
    next_state = reducer(initial_state, action)
    vote = next_state['vote']
    assert vote['pair'] == ('Trainspotting', '28 Days Later')
    assert vote['tally'] == {'Trainspotting': 1}


def test_should_work_with_none_state():
    action = {'type': 'SET_ENTRIES', 'entries': ['Trainspotting']}
    next_state = reducer(None, action)
    assert next_state['entries'] == ('Trainspotting',)


def test_can_be_used_with_reduce():
    actions = [
        {'type': 'SET_ENTRIES', 'entries': ['Trainspotting', '28 Days Later']},
        {'type': 'NEXT'},
        {'type': 'VOTE', 'entry': 'Trainspotting'},
        {'type': 'VOTE', 'entry': '28 Days Later'},
        {'type': 'VOTE', 'entry': 'Trainspotting'},
        {'type': 'NEXT'}
    ]
    final_state = functools.reduce(reducer, actions)
    assert final_state['winner'] == 'Trainspotting'
