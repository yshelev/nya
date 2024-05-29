class User:
	def __init__(self, login, password, number):
		self.__login = login
		self.__password = password
		self.__number = number

	def check_password(self, password: str):
		return self.__password == password

	def get_login(self):
		return self.__login

	