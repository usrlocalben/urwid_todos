from urwid import WidgetPlaceholder, Text


class Todo(WidgetPlaceholder):
    def __init__(self, on_click, completed, text):
        self.on_click = on_click
        if completed:
            self.widget = Text('[X] --' + text + '--')
        else:
            self.widget = Text('[ ]   ' + text)
        super(Todo, self).__init__(self.widget)

    def mouse_event(self, size, event, button, col, row, focus):
        if event == 'mouse release' and button == 0:
            self.on_click()
            return True
