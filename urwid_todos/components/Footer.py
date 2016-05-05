from urwid_todos.containers.FilterButton import FilterButton
from urwid import Pile, Text, Padding, CENTER
from urwid_pydux import Component


class Footer(Component):
    def render_component(self, store, props):
        return Pile([
            Text('Show:'),
            Padding(Pile([
                FilterButton(store=store,
                             filter='SHOW_ALL', text='All'),

                FilterButton(store=store,
                             filter='SHOW_ACTIVE', text='Active'),

                FilterButton(store=store,
                             filter='SHOW_COMPLETED', text='Completed'),
            ]), align=CENTER, left=4, right=4)
        ])
