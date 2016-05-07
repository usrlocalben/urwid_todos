from urwid import Edit, Button, Columns, Text
from urwid_pydux import ConnectedComponent

from urwid_todos.actions import add_todo


class AddTodo(ConnectedComponent):
    def render_component(self, props):
        self.edit = Edit(caption='Todo: ', edit_text='')
        self.button = Button('Add Todo')
        return Columns([
            (1, Text('[')),
            self.edit,
            (1, Text(']')),
            (18, self.button),
        ])

    def keypress(self, size, key):
        if key == 'enter':
            self.on_submit()
            return True
        return super(AddTodo, self).keypress(size, key)

    def on_submit(self):
        if not self.edit.get_edit_text().strip():
            return
        self.store['dispatch'](add_todo(self.edit.get_edit_text()))
        self.edit.set_edit_text('')

    def on_click(self, *args):
        self.on_submit()

