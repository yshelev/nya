from WindowsScripts.main_window import *
from DataClasses.Constants import *


class EmployerWindow(WindowWorker):
	def __init__(self, parent: WindowWorker, *args):
		try:
			super().__init__()
			self.par = parent
			uic.loadUi(self.fileFinder.get_file_from_WindowsUI("employer.ui"), self)

			self.cities = self.par.cities

			self.cities["все"] = ["все"]

			self.fill_combo_box(self.professionBox, PROFESSIONS + FILTER_COMBO_BOX_ALL, ALL)
			self.fill_combo_box(self.cityBox, FILTER_COMBO_BOX_ALL, ALL)
			self.fill_combo_box(self.countryBox, list(self.cities.keys()) + FILTER_COMBO_BOX_ALL, ALL)

			self.fill_table_with_data(self.table, self.par.employers, title=EMPLOYERS_TABLE_TITLE)

			self.set_current_text_changed_on_several_combo_boxes(
				[
					(self.countryBox, self.on_combo_box_countries_changed)
				]
			)

			self.set_on_click_on_several_buttons(
				[
					(self.backButton, self.finish),
					(self.filterButton, self.filter_)
				]
			)
		except Exception as e:
			print(e)

	def on_combo_box_countries_changed(self) -> None:
		currentCountry = self.countryBox.currentText()
		data = self.cities[currentCountry]
		self.fill_combo_box(
			self.cityBox,
			data + (FILTER_COMBO_BOX_ALL if currentCountry != "все" and currentCountry != "-" else []),
			data[0]
		)

	def filter_(self):
		for i in range(self.table.rowCount()):
			if self.check_row(*[self.table.item(i, j).text() for j in range(0, self.table.columnCount())]):
				self.table.setRowHidden(i, False)
			else:
				self.table.setRowHidden(i, True)

	def check_row(self, number, profession, country, city, *args):
		profession_combo_box_data = self.professionBox.currentText()
		city_combo_box_data = self.cityBox.currentText()
		country_combo_box_data = self.countryBox.currentText()

		profession_output = (
			(profession_combo_box_data == profession)
			or
			(profession_combo_box_data == "все")
		)

		city_output = (
			(city_combo_box_data == city)
			or
			(city_combo_box_data == "все")
		)

		country_output = (
			(country_combo_box_data == country)
			or
			(country_combo_box_data == "все")
		)

		return profession_output and city_output and country_output

	def finish(self):
		self.par.show()
		self.destroy()
