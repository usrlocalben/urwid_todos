import urwid
from pydux.create_store import create_store
from urwid_pydux import subscribe_urwid_redraw

from components.App import App
from reducers import todo_app


def main():
    store = create_store(todo_app)
    root = App(store=store)
    loop = urwid.MainLoop(root)
    subscribe_urwid_redraw(store, loop)
    loop.run()


if __name__ == '__main__':
    main()
