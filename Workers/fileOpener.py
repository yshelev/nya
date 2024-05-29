import json
import sqlite3


class FileOpener:
	def __init__(self):
		self.encoding = "UTF-8"
		self.read_mode = "r"
		self.write_mode = "w"

	def jsonToDict(self, path_to_json_file: str) -> dict:
		with open(path_to_json_file, self.read_mode, encoding=self.encoding) as filePointer:
			return json.load(filePointer)

	def sqliteToList(self, path_to_db: str, query: str) -> list:
		connection = sqlite3.connect(path_to_db)
		cursor = connection.cursor()

		query_result = cursor.execute(query).fetchall()

		return query_result

	def userToSqlite(self, path_to_db: str, query: str) -> None:
		connection = sqlite3.connect(path_to_db)
		cursor = connection.cursor()

		cursor.execute(query)

		connection.commit()
		connection.close()

