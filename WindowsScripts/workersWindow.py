from PyQt5 import uic
from Workers.windowWorker import WindowWorker


class WorkersWindow(WindowWorker):
	def __init__(self, parent: WindowWorker, *args):
		super().__init__()
		self.par = parent
		uic.loadUi(self.fileFinder.get_file_from_WindowsUI("worker.ui"), self)

		self.cities = self.par.cities

		# заполнение комбо боксов начальными значениями
		self.fill_combo_box(self.comboBox_cities, ["-"], "-")
		self.fill_combo_box(self.comboBox_countries, self.cities.keys(), "-")

		# установка сигналов на комбо боксы
		self.set_current_text_changed_on_several_combo_boxes(
			[
				(self.comboBox_countries, self.on_combo_box_countries_changed)
			]
		)

		# установка сигналов на кнопки
		self.set_on_click_on_several_buttons(
			[
				(self.pushButton_continue, self.on_confirm),
				(self.pushButton_cancel, self.on_cancel)
			]
		)

		self.label_warning_no_user.hide()
		self.label_warning_personal_info.hide()

	def on_combo_box_countries_changed(self) -> None:
		# при смене данных в комбо боксе страны так же меняем данные для комбо боксов городов
		currentCountry = self.comboBox_countries.currentText()
		data = self.cities[currentCountry]
		self.fill_combo_box(self.comboBox_cities, data, data[0])

	def on_confirm(self):
		# собираем информацию о заполненную информацию о работнике
		agreement_personal_info = self.radioButton_personal_info.isChecked()
		profession = self.professions.checkedButton().text()
		is_need_dormitory = self.radioButton_2.isChecked()
		country = self.comboBox_countries.currentText() if is_need_dormitory else "-"
		city = self.comboBox_cities.currentText() if is_need_dormitory else "-"
		about_user = self.textEdit.toPlainText()

		user = self.par.current_user

		# если не стоит галочка для показа персональной информации, выходим
		if not agreement_personal_info:
			self.label_warning_personal_info.show()
			self.label_warning_no_user.hide()
			return

		# если пользователь не зарегистрирован, выходим
		if not user:
			self.label_warning_no_user.show()
			self.label_warning_personal_info.hide()
			return

		user = self.par.current_user
		number = user.get_number()
		id_, _, password = \
			self.fileOpener.sqliteToList(self.fileFinder.get_file_from_data_files("employers.db"), f"""
					SELECT *
					FROM Users 
					WHERE phone_number = "{number}"
				""")[0]

		info = [
			profession,
			country,
			city,
			about_user
		]

		self.par.append_employer(id_, number, password, info)

		self.finish()

	def on_cancel(self):
		self.finish()

	def finish(self):
		self.par.show()
		self.destroy()
