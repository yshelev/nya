from WindowsScripts.main_window import *


class WorkersWindow(WindowWorker):
	def __init__(self, parent: MainWindow, *args):
		super().__init__()
		self.par = parent
		uic.loadUi(self.fileFinder.get_file_from_WindowsUI("worker.ui"), self)

		self.fill_combo_box(self.comboBox_countries, self.cities.keys(), "-")
		self.fill_combo_box(self.comboBox_cities, ["-"], "-")

		self.set_current_text_changed_on_several_combo_boxes(
			[
				(self.comboBox_countries, self.on_combo_box_countries_changed)
			]
		)

	def on_combo_box_countries_changed(self):
		currentCountry = self.comboBox_countries.currentText()
		data = self.cities[currentCountry]
		self.fill_combo_box(self.comboBox_cities,  data, data[0])



