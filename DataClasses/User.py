class User:
	def __init__(self, id_, number, password):
		self.__id = id_
		self.__password = password
		self._number = number

	def check_password(self, password: str):
		return self.__password == password

	def get_number(self):
		return self._number

	def get_id(self):
		return self.__id

	def __repr__(self):
		num1 = self._number[0]
		num2 = self._number[1:4]
		num3 = self._number[4:7]
		num4 = self._number[7:9]
		num5 = self._number[9:11]
		return f"+{num1}({num2}) {num3}-{num4}-{num5}: {self.__password}"
