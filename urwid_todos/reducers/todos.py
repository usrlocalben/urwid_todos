from pydux.extend import extend


def todo(state=None, action=None):
    if action['type'] == 'ADD_TODO':
        return {
            'id': action['id'],
            'text': action['text'],
            'completed': False,
        }
    elif action['type'] == 'TOGGLE_TODO':
        if state['id'] != action['id']:
            return state
        else:
            return extend(
                state,
                {'completed': not state['completed']}
            )
    else:
        return state


def todos(state=None, action=None):
    if state is None:
        state = []
    if action['type'] == 'ADD_TODO':
        return state + [todo(None, action)]
    if action['type'] == 'TOGGLE_TODO':
        return [todo(t, action) for t in state]
    return state
