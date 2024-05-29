import json
import sqlite3


class FileOpener:
	def __init__(self):
		pass

	def jsonToDict(self, path_to_json_file: str) -> dict:
		with open(path_to_json_file, "r", encoding="UTF-8") as filePointer:
			return json.load(filePointer)

	def sqliteToDict(self, path_to_db: str, query: str) -> list:
		connection = sqlite3.connect(path_to_db)
		cursor = connection.cursor()

		query_result = cursor.execute(query).fetchall()

		return query_result
