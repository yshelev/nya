from Workers.windowWorker import WindowWorker
from PyQt5 import uic
import re
from DataClasses.User import User
from DataClasses.Constants import *


class SignWindow(WindowWorker):
	def __init__(self, parent: WindowWorker, *args):
		super().__init__()
		self.par = parent
		uic.loadUi(self.fileFinder.get_file_from_WindowsUI("sign.ui"), self)

		# установка сигналов на кнопки
		self.set_on_click_on_several_buttons(
			[
				(self.pushButton_registration, self.on_authorization_click),
				(self.pushButton_signin, self.on_sign_in_click),
				(self.returnButton, self.finish)
			]
		)

	def on_sign_in_click(self):
		# получение информации о пытающемся войти в аккаунт пользователе
		number = self.textEdit_login.toPlainText()
		password = self.textEdit_password.toPlainText()
		number = "".join(re.split(fr"[{SYMBOLS_TO_DELETE_FROM_NUMBER}]+", number))

		# если пользователь существует, входим
		for user in self.par.users:
			if user.get_number() == number:
				if user.check_password(password):
					self.par.set_current_user(user)
					self.finish()

				self.label_warning.setText(PASSWORD_NOT_MATCH)
				break

		# если пользователь не существует, показываем текст с ошибкой
		self.label_warning.setText(NO_USER_WITH_PHONE_NUMBER)

	def on_authorization_click(self):
		# получение информации о пытающемся авторизироваться пользователе
		number = self.textEdit_login.toPlainText()
		password = self.textEdit_password.toPlainText()
		number = "".join(re.split(fr"[{SYMBOLS_TO_DELETE_FROM_NUMBER}]+", number))

		# проверка исключений
		if len(number) != CURRENT_NUMBER_LENGTH:
			self.label_warning.setText(INCORRECT_NUMBER)
			return

		for user in self.par.users:
			if user.get_number() == number:
				self.label_warning.setText(USER_IS_ALREADY_REGISTERED)
				return

		if password == "":
			self.label_warning.setText(INCORRECT_PASSWORD)
			return

		# добавление пользователя
		self.par.append_user(number, password)
		self.par.set_current_user(User(number, password))
		self.finish()

	def finish(self):
		self.par.show()
		self.destroy()
