"""
Real-world use:
Stack → Undo/Redo in a text editor.

The most recent action is stored on top of the stack,
so the latest action can be undone first.
"""

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []

    def type(self, characters):
        self.undo_stack.append(self.text)
        self.text += characters

    def undo(self):
        if self.undo_stack:
            self.text = self.undo_stack.pop()


editor = TextEditor()

editor.type("A")
editor.type("B")
editor.type("C")

print(editor.text)   # ABC

editor.undo()
print(editor.text)   # AB

editor.undo()
print(editor.text)   # A