from DataClasses.User import User
from Workers.filePathFinder import FileFinder
from Workers.fileOpener import FileOpener

from PyQt5.QtWidgets import *


class WindowWorker(QMainWindow):
	def __init__(self):
		super().__init__()
		self.fileFinder = FileFinder()
		self.fileOpener = FileOpener()

	def set_on_click_on_several_buttons(self, button_function: list[tuple]) -> None:
		for button, function in button_function:
			button.clicked.connect(function)

	def set_current_text_changed_on_several_combo_boxes(self, comboBox_function: list[tuple]) -> None:
		for comboBox, function in comboBox_function:
			comboBox.currentTextChanged.connect(function)

	def set_toggled_on_several_radio_button(self, radioButton_function: list[tuple]) -> None:
		for radioButton, function in radioButton_function:
			radioButton.toggled.connect(function)

	def fill_combo_box(self, combo_box: QComboBox, data: list, start_value: str):
		combo_box.clear()
		combo_box.addItems(data)
		combo_box.setCurrentText(start_value)

