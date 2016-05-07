from urwid import ListBox, SimpleListWalker
from urwid_pydux import Component

from .Todo import Todo


class TodoList(Component):
    prop_types = {
        'todos': list,
        'on_todo_click': callable,
    }

    def render_component(self, props):

        def make_todo(id, completed, text):
            def on_click():
                props['on_todo_click'](id)
            return Todo(
                on_click=on_click,
                completed=completed,
                text=text,
            )

        return ListBox(SimpleListWalker(
            [make_todo(**todo) for todo in props['todos']]
        ))
