from urwid import Text, Button
from urwid_pydux import Component


class Link(Component):
    prop_types = {
        'active': bool,
        'text': basestring,
        'on_click': callable,
    }

    def render_component(self, props):
        if props['active']:
            widget = Text(props['text'])
        else:
            widget = Button(props['text'], on_press=lambda _: props['on_click']())
        return widget
