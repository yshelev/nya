class User:
	def __init__(self, number, password):
		self.__password = password
		self.__number = number

	def check_password(self, password: str):
		return self.__password == password

	def get_number(self):
		return self.__number

	def __repr__(self):
		num1 = self.__number[0]
		num2 = self.__number[1:4]
		num3 = self.__number[4:7]
		num4 = self.__number[7:9]
		num5 = self.__number[9:11]
		return f"+{num1}({num2}) {num3}-{num4}-{num5}: {self.__password}"
