next_id = [0]  # r/w closure
def add_todo(text):
    next_id[0] += 1
    return {'type': 'ADD_TODO', 'id': next_id[0], 'text': text}


def toggle_todo(id_):
    return {'type': 'TOGGLE_TODO', 'id': id_}


def set_visibility_filter(filter_):
    return {'type': 'SET_VISIBILITY_FILTER', 'filter': filter_}
