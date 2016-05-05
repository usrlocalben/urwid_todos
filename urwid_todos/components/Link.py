from urwid import WidgetPlaceholder, Text, Button


class Link(WidgetPlaceholder):
    def __init__(self, active, text, on_click):
        self.active = active
        self.on_click = on_click
        if active:
            widget = Text(text)
        else:
            widget = Button(text, on_press=lambda _: on_click())
        super(Link, self).__init__(widget)
