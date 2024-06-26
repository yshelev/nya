from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox

from DataClasses.User import User
from DataClasses.Employer import Employer
from Workers.windowWorker import WindowWorker
from WindowsScripts.workersWindow import WorkersWindow
from WindowsScripts.employerWindow import EmployerWindow
from WindowsScripts.signWindow import SignWindow


class MainWindow(WindowWorker):
    def __init__(self):
        super().__init__()
        uic.loadUi(self.fileFinder.get_file_from_WindowsUI("menu.ui"), self)

        # установка сигналов на кнопки
        # если на кнопку нужно установить сигнал, надо добавить пару (кнопка, функция) в список
        self.set_on_click_on_several_buttons(
            [
                (self.employ_btn, self.on_employ_button_click),
                (self.work_btn, self.on_work_button_click),
                (self.sign_btn, self.on_sign_click)
            ],
        )

        # заполнение списка пользователей и работников данными из бд
        users_query_result = self.fileOpener.sqliteToList(
            self.fileFinder.get_file_from_data_files("employers.db"),
            f"""
                SELECT phone_number, password FROM Users
            """
        )

        employer_query_result = self.fileOpener.sqliteToList(
            self.fileFinder.get_file_from_data_files("employers.db"),
            f"""
                SELECT Employers.user_id, Users.phone_number, Users.password, Employers.profession, Employers.country, Employers.city, Employers.user_about
                FROM Employers
                INNER JOIN Users 
                ON Users.id = Employers.user_id
            """
        )

        self.current_user = None

        self.users = [
            User(*item) for item in users_query_result
        ]

        self.employers = [
            Employer(*item) for item in employer_query_result
        ]

        # заполнение списка городов данными из json
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

    def append_employer(self, id_: int, number: str, password: str, employer_info: list) -> None:
        # добавление работника в список работников в программе
        self.employers.append(Employer(id_, number, password, *employer_info))

        # получение информации о работника
        employer_info = [id_] + employer_info

        # перевод информации в формат sqlite
        sqlite_info = "\"" + "\", \"".join(list(map(lambda x: str(x), employer_info))) + "\""

        # добавление информации про работника в бд
        self.fileOpener.userToSqlite(self.fileFinder.get_file_from_data_files("employers.db"), f"""
            INSERT INTO Employers (user_id, profession, country, city, user_about)
            VALUES ({sqlite_info})
        """)

    def append_user(self, number: str, password: str) -> None:
        # добавление пользователя в список работников в программе
        self.users.append(User(number, password))

        # добавление информации про пользователя в бд
        self.fileOpener.userToSqlite(self.fileFinder.get_file_from_data_files("employers.db"), f"""
            INSERT INTO Users (phone_number, password)
            VALUES ({number}, {password})
        """)
