from urwid_pydux import Component

from urwid_todos.actions import set_visibility_filter
from urwid_todos.components.Link import Link


class FilterButton(Component):
    def __init__(self, store, filter, text):
        self.filter = filter
        self.text = text
        super(FilterButton, self).__init__(store)

    def map_state_to_props(self, state):
        return {
            'active': self.filter == state['visibility_filter']
        }

    def map_dispatch_to_props(self, dispatch):
        def on_click():
            dispatch(set_visibility_filter(self.filter))
        return {
            'on_click': on_click,
        }

    def render_component(self, store, props):
        return Link(props['active'], self.text, props['on_click'])