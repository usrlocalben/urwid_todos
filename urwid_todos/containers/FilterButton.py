from urwid_pydux import ConnectedComponent

from urwid_todos.actions import set_visibility_filter
from urwid_todos.components.Link import Link


class FilterButton(ConnectedComponent):
    prop_types = {
        'filter': basestring,
        'text': basestring,
    }

    def map_state_to_props(self, state, own_props):
        return {'active': own_props['filter'] == state['visibility_filter']}

    def map_dispatch_to_props(self, dispatch, own_props):
        def on_click():
            dispatch(set_visibility_filter(own_props['filter']))
        return {'on_click': on_click}

    def render_component(self, props):
        return Link(
            active=props['active'],
            text=props['text'],
            on_click=props['on_click'],
        )
