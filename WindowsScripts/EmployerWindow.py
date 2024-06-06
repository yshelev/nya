from WindowsScripts.main_window import *
from DataClasses.Constants import *


class EmployerWindow(WindowWorker):
	def __init__(self, parent: WindowWorker, *args):
		super().__init__()
		self.par = parent
		uic.loadUi(self.fileFinder.get_file_from_WindowsUI("employer.ui"), self)

		self.fill_table_with_data(self.table, self.par.employers, title=EMPLOYERS_TABLE_TITLE)