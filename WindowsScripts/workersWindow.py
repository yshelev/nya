from WindowsScripts.main_window import *


class WorkersWindow(WindowWorker):
	def __init__(self, parent: MainWindow, *args):
		super().__init__()
		self.par = parent
		uic.loadUi(self.fileFinder.get_file_from_WindowsUI("worker.ui"), self)

		self.fill_combo_box(self.comboBox_countries, self.cities.keys(), "-")
		self.fill_combo_box(self.comboBox_cities, ["-"], "-")




