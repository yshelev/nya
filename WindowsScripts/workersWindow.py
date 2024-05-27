from WindowsScripts.main_window import *


class WorkersWindow(WindowWorker):
	def __init__(self, parent: MainWindow, *args):
		super().__init__()
		self.par = parent
		uic.loadUi(self.fileFinder.get_file_from_WindowsUI("worker.ui"), self)

		# fill combo boxes with start values
		self.fill_combo_box(self.comboBox_cities, ["-"], "-")
		self.fill_combo_box(self.comboBox_countries, self.cities.keys(), "-")

		# set signals to comboBoxes
		self.set_current_text_changed_on_several_combo_boxes(
			[
				(self.comboBox_countries, self.on_combo_box_countries_changed)
			]
		)

		self.set_on_click_on_several_buttons(
			[
				(self.pushButton_continue, self.on_confirm),
				(self.pushButton_cancel, self.on_cancel)
			]
		)

	def on_combo_box_countries_changed(self) -> None:
		currentCountry = self.comboBox_countries.currentText()
		data = self.cities[currentCountry]
		self.fill_combo_box(self.comboBox_cities, data, data[0])

	def on_confirm(self):
		agreement_personal_info = self.radioButton_personal_info.isChecked()

		if agreement_personal_info:
			profession = self.professions.checkedButton().text()
			is_need_dormitory = self.radioButton_2.isChecked()
			country = self.comboBox_countries.currentText() if is_need_dormitory else "-"
			city = self.comboBox_cities.currentText() if is_need_dormitory else "-"
			about_user = self.textEdit.toPlainText()

			info = (
				profession,
				country,
				city,
				about_user
			)

			self.finish()

	def on_cancel(self):
		self.finish()

	def finish(self):
		self.par.show()
		self.destroy()
