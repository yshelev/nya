from Workers.filePathFinder import FileFinder
from Workers.fileOpener import FileOpener

from PyQt5.QtWidgets import *


class WindowWorker(QMainWindow):
	def __init__(self):
		super().__init__()
		self.fileFinder = FileFinder()
		self.fileOpener = FileOpener()
		self.cities = self.fileOpener.jsonToDict(
			self.fileFinder.get_file_from_data_files("cities.json")
		)
		self.cities["-"] = ["-"]


	def set_on_click_on_several_buttons(self, button_function: list[tuple]) -> None:
		for button, function in button_function:
			button.clicked.connect(function)

	def fill_combo_box(self, combo_box: QComboBox, data: list, start_value: str):
		combo_box.clear()
		combo_box.addItems(data)
		combo_box.setCurrentText(start_value)
