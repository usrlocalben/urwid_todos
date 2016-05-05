def visibility_filter(state=None, action=None):
    if state is None:
        state = 'SHOW_ALL'
    if action['type'] == 'SET_VISIBILITY_FILTER':
        return action['filter']
    return state
