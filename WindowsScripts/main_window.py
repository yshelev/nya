from os import path
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from Workers.windowWorker import WindowWorker
from WindowsScripts.workersWindow import WorkersWindow
from WindowsScripts.employerWindow import EmployerWindow


class MainWindow(WindowWorker):
    def __init__(self):
        super().__init__()
        uic.loadUi(self.fileFinder.get_file_from_WindowsUI("menu.ui"), self)

        # setting on clicks. If you need set +1, just add (button, on_click)
        self.set_on_click_on_several_buttons(
            [
                (self.employ_btn, self.on_employ_button_click),
                (self.work_btn, self.on_work_button_click)
            ],
        )

    def on_employ_button_click(self):
        self.start_window_children(EmployerWindow)

    def on_work_button_click(self):
        self.start_window_children(WorkersWindow)

    def start_window_children(self, class_: type):
        self.temp = class_(self)
        self.temp.show()
        self.hide()