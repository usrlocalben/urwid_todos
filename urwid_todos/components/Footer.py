from urwid_todos.containers.FilterButton import FilterButton
from urwid import Pile, Text, Padding, CENTER
from urwid_pydux import ConnectedComponent


class Footer(ConnectedComponent):
    def render_component(self, props):
        return Pile([
            Text('Show:'),
            Padding(Pile([
                FilterButton(store=props['store'],
                             filter='SHOW_ALL', text='All'),

                FilterButton(store=props['store'],
                             filter='SHOW_ACTIVE', text='Active'),

                FilterButton(store=props['store'],
                             filter='SHOW_COMPLETED', text='Completed'),
            ]), align=CENTER, left=4, right=4)
        ])
