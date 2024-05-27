import json


class FileOpener:
	def __init__(self):
		pass

	def jsonToDict(self, path_to_json_file: str) -> dict:
		with open(path_to_json_file, "r", encoding="UTF-8") as filePointer:
			return json.load(filePointer)
