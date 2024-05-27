from os import path
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from Workers.fileWorker import FileWorker


class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.fileWorker = FileWorker()
        uic.loadUi(self.fileWorker.get_file_from_WindowsUI("menu.ui"))



