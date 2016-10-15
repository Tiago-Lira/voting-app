
from copy import deepcopy


def reducer(state, action_data):
    if state is None:
        state = dict()
    action_data = deepcopy(action_data)
    action_type = action_data.pop('type').upper()
    action_func = action.pick(action_type)
    return action_func(state, **action_data)


def action_factory():
    ACTION_MAP = {}

    def pick(action_type):
        nonlocal ACTION_MAP
        return ACTION_MAP.get(action_type)

    def register(action_type, partial_state=None):
        nonlocal ACTION_MAP

        def decorator(fn):
            def redux_state(state, *args, **kwargs):
                if partial_state:
                    state = deepcopy(state)
                    fn_state = state.get(partial_state)
                    state[partial_state] = fn(fn_state, *args, **kwargs)
                    return state
                else:
                    return fn(state, *args, **kwargs)

            ACTION_MAP[action_type.upper()] = redux_state
            return fn
        return decorator

    return type('Action', (), {'register': register, 'pick': pick})


def make_store():
    previous_states = ()
    current_state = {}

    def get_state():
        nonlocal current_state
        return deepcopy(current_state)

    def store_previous_state(state):
        nonlocal previous_states
        previous_states += (state,)

    def dispatch(action):
        nonlocal current_state
        state = get_state()
        store_previous_state(state)
        current_state = reducer(state, action)

    return type('Store', (), {'dispatch': dispatch, 'get_state': get_state})


action = action_factory()
