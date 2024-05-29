from os import path
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from DataClasses.User import User
from Workers.windowWorker import WindowWorker
from WindowsScripts.workersWindow import WorkersWindow
from WindowsScripts.employerWindow import EmployerWindow
from WindowsScripts.signWindow import SignWindow


class MainWindow(WindowWorker):
    def __init__(self):
        super().__init__()
        uic.loadUi(self.fileFinder.get_file_from_WindowsUI("menu.ui"), self)

        # setting on clicks. If you need set +1, just add (button, on_click)
        self.set_on_click_on_several_buttons(
            [
                (self.employ_btn, self.on_employ_button_click),
                (self.work_btn, self.on_work_button_click),
                (self.sign_btn, self.on_sign_click)
            ],
        )

        query_result = self.fileOpener.sqliteToList(
            self.fileFinder.get_file_from_data_files("employers.db"),
            f"""
                SELECT phone_number, password FROM Users
            """
        )

        self.current_user = None

        self.users = [
            User(*item) for item in query_result
        ]

        self.cities = self.fileOpener.jsonToDict(
            self.fileFinder.get_file_from_data_files("cities.json")
        )
        self.cities["-"] = ["-"]

    def on_employ_button_click(self):
        self.start_window_children(EmployerWindow)

    def on_work_button_click(self):
        self.start_window_children(WorkersWindow)

    def on_sign_click(self):
        self.start_window_children(SignWindow)

    def start_window_children(self, class_: type):
        self.temp = class_(self)
        self.temp.show()
        self.hide()

    def set_current_user(self, user: User):
        self.current_user = user

    def append_user(self, number: str, password: str) -> None:
        self.users.append(User(number, password))
        self.fileOpener.userToSqlite(self.fileFinder.get_file_from_data_files("employers.db"), f"""
            INSERT INTO Users (phone_number, password)
            VALUES ({number}, {password})
        """)
