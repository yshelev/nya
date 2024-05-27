from os import path
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from Workers.fileWorker import FileWorker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__fileWorker = FileWorker()
        uic.loadUi(self.__fileWorker.get_file_from_WindowsUI("menu.ui"), self)

        # setting on clicks. If you need set +1, just add (button, on_click)
        self.set_on_click_on_several_buttons(
            [
                (self.employ_btn, self.on_employ_button_click),
                (self.work_btn, self.on_work_button_click)
            ],
        )

    def set_on_click_on_several_buttons(self, button_function: list[tuple]) -> None:
        for button, function in button_function:
            button.clicked.connect(function)

    def on_employ_button_click(self):
        print(1)

    def on_work_button_click(self):
        print(2)



