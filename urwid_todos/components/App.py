from urwid_todos.containers.AddTodo import AddTodo
from urwid_todos.containers.VisibleTodoList import VisibleTodoList
from urwid import Overlay, Frame, SolidFill, CENTER, RELATIVE, MIDDLE
from urwid_pydux import ConnectedComponent
from .Footer import Footer


class App(ConnectedComponent):
    def render_component(self, props):
        return Overlay(
            top_w=Frame(
                header=AddTodo(store=props['store']),
                body=VisibleTodoList(store=props['store']),
                footer=Footer(store=props['store']),
                focus_part='header',
            ),
            bottom_w=SolidFill(u'\N{MEDIUM SHADE}'),
            align=CENTER,
            width=(RELATIVE, 40),
            valign=MIDDLE,
            height=(RELATIVE, 60),
            min_width=20,
            min_height=20,
        )
