from urwid import WidgetPlaceholder, ListBox, SimpleListWalker

from .Todo import Todo


class TodoList(WidgetPlaceholder):
    def __init__(self, todos, on_todo_click):

        def make_todo(id, completed, text):
            def on_click():
                on_todo_click(id)
            return Todo(on_click, completed, text)

        widget = ListBox(SimpleListWalker(
            [make_todo(**todo) for todo in todos]
        ))
        super(TodoList, self).__init__(widget)

