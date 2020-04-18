from abc import ABC, abstractclassmethod


class UIControl(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print('TextBook')


class DropDownList(UIControl):
    def draw(self):
        print('DropDownList')


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])
