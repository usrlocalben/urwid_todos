from urwid_pydux import Component

from urwid_todos.components.TodoList import TodoList
from urwid_todos.actions import toggle_todo


def get_visible_todos(todos, filter):
    if filter == 'SHOW_ALL':
        return todos
    elif filter == 'SHOW_COMPLETED':
        return [t for t in todos if t['completed']]
    elif filter == 'SHOW_ACTIVE':
        return [t for t in todos if not t['completed']]
    else:
        msg = 'Unknown filter "{}"'.format(filter)
        raise Exception(msg)


class VisibleTodoList(Component):
    def map_state_to_props(self, state):
        return {
            'todos': get_visible_todos(todos=state['todos'],
                                       filter=state['visibility_filter'])
        }

    def map_dispatch_to_props(self, dispatch):
        def on_todo_click(id):
            dispatch(toggle_todo(id))
        return {
            'on_todo_click': on_todo_click
        }

    def render_component(self, store, props):
        return TodoList(props['todos'], props['on_todo_click'])
