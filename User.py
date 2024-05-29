class User:
	def __init__(self, password, number):
		self.__password = password
		self.__number = number

	def check_password(self, password: str):
		return self.__password == password

	def get_number(self):
		return self.__number
