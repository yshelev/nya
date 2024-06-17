from DataClasses.User import User


class Employer(User):
	def __init__(self, id_, number, password, profession, country, city, user_about):
		super().__init__(number, password)
		self.user_id = id_
		self.profession = profession
		self.country = country
		self.city = city
		self.user_about = user_about
		self.data = [self.get_number(), self.profession, self.country, self.city, self.user_about]
		self.data_index = 0
		self.stop_data_index = 5

	"""
	__iter__ и __next__ для итерации по self.data
	"""
	def __iter__(self):
		self.data_index = -1
		return self

	def __next__(self):
		self.data_index += 1
		if self.data_index == self.stop_data_index:
			raise StopIteration
		return self.data[self.data_index]