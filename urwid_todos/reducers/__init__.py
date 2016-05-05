from pydux.combine_reducers import combine_reducers

from .todos import todos
from .visibility_filter import visibility_filter


todo_app = combine_reducers({
    'todos': todos,
    'visibility_filter': visibility_filter,
})
