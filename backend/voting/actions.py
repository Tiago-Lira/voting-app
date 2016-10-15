
from copy import deepcopy
from .redux import action


@action.register('SET_ENTRIES')
def set_entries(state, entries):
    state = deepcopy(state)
    state['entries'] = tuple(entries)
    return state


@action.register('NEXT')
def next_pair(state):

    def decide_winner(entry1, entry2, tally):
        quantity1 = int(tally.get(entry1, 0))
        quantity2 = int(tally.get(entry2, 0))
        if quantity1 > quantity2:
            return entry1
        elif quantity1 < quantity2:
            return entry2
        return None

    state = deepcopy(state)
    entries = list(state.pop('entries', []))
    vote = state.pop('vote', {})
    tally = vote.pop('tally', {})

    if 'pair' in vote:
        entry1, entry2 = vote.pop('pair')
        winner = decide_winner(entry1, entry2, tally)

        if not entries and winner:
            state['winner'] = winner
            return state

        elif entries and winner == entry1:
            entries.append(entry1)
        elif entries and winner == entry2:
            entries.append(entry2)
        else:
            entries.append(entry1)
            entries.append(entry2)

    entry1 = entries.pop(0)
    entry2 = entries.pop(0)
    vote['pair'] = (entry1, entry2)
    state['vote'] = vote
    state['entries'] = tuple(entries)
    return state


@action.register('VOTE', partial_state='vote')
def vote(state, entry):
    state = deepcopy(state)
    tally = state.pop('tally', {})

    entry_votes = tally.get(entry, 0)
    entry_votes += 1

    tally[entry] = entry_votes
    state['tally'] = tally
    return state
