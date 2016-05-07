from urwid import Text
from urwid_pydux import Component


class Todo(Component):
    prop_types = {
        'on_click': callable,
        'completed': bool,
        'text': basestring,
    }

    def component_will_mount(self, props):
        self.on_click = props['on_click']

    def render_component(self, props):
        if props['completed']:
            return Text('[X] --' + props['text'] + '--')
        else:
            return Text('[ ]   ' + props['text'])

    def mouse_event(self, size, event, button, col, row, focus):
        if event == 'mouse release' and button == 0:
            self.on_click()
            return True
