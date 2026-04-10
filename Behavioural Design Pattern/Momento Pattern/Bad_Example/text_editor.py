from collections import deque

class TextEditor:
    def __init__(self):
        self.__text = ""
        self.stack = deque()

    def write(self, new_text):
        self.__text += new_text
        self.stack.append(self.__text)

    def get_text(self):
        return self.stack[-1]
    
    def undo(self):
        self.stack.pop()    

    
text_editor = TextEditor()
text_editor.write("Hello")
text_editor.write(" World")
text_editor.write(" GoodBye")
print(text_editor.get_text())
text_editor.undo()
print(text_editor.get_text())
        