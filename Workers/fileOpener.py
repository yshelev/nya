import json
import sqlite3


class FileOpener:
	def __init__(self):
		self.encoding = "UTF-8"
		self.read_mode = "r"
		self.write_mode = "w"

	def jsonToDict(self, path_to_json_file: str) -> dict:
		"""
		returns data from path_to_json_file in dict presentation
		"""
		with open(path_to_json_file, self.read_mode, encoding=self.encoding) as filePointer:
			return json.load(filePointer)

	@staticmethod
	def sqliteToList(path_to_db: str, query: str) -> list:
		"""
		returns data from db located in path_to_db on query in list presentation
		"""
		connection = sqlite3.connect(path_to_db)
		cursor = connection.cursor()

		query_result = cursor.execute(query).fetchall()

		connection.close()
		return query_result

	@staticmethod
	def userToSqlite(path_to_db: str, query: str) -> None:
		"""
		записывает query в path_to_db
		"""
		connection = sqlite3.connect(path_to_db)
		cursor = connection.cursor()

		cursor.execute(query)

		connection.commit()
		connection.close()

	def set_encoding(self, encoding: str) -> None:
		self.encoding = encoding

