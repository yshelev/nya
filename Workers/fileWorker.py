class FileWorker:
	"""
	class with methods which returns path to files
	"""

	def __init__(self):
		self.ASSETS = "Assets/"
		self.WINDOWSUI = "WindowsUI/"

	def get_file_in_directory(self, filename: str) -> str:
		"""
		returns path to file located in same directory/start directory with filename
		:param filename:
		:return:
		"""
		return filename

	def get_file_from_assets(self, filename: str) -> str:
		"""
		returns path to file located in 'Assets' directory with filename
		:param filename:
		:return:
		"""
		return self.ASSETS + filename

	def get_file_from_WindowsUI(self, filename: str) -> str:
		"""
		returns path to file located in 'WindowsUI' directory with filename
		:param filename:
		:return:
		"""
		return self.ASSETS + self.WINDOWSUI + filename



