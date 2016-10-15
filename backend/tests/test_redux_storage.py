
from voting.redux import make_store


def test_build_store():
    store = make_store()
    assert store.get_state() == {}

    store.dispatch({
        'type': 'SET_ENTRIES',
        'entries': ['Trainspotting', '28 Days Later']
    })

    assert store.get_state() == {'entries': ('Trainspotting', '28 Days Later')}
