from core.window import Window

class Errors:
	def __init__(self):
		self.errors_list = list()
		self.some_fatals = False


	def add_error(self, error_msg, fatal=False):
		self.some_fatals = max(self.some_fatals, fatal)
		self.errors_list.append('– ' + error_msg)


	def is_empty(self):
		return len(self.errors_list) == 0


	def show_errors(self):
		if Window.MainWindow is not None:
			if not self.is_empty():
				pass_list = list(self.errors_list)
				self.errors_list = list()
				title = _('Warning') if not self.some_fatals else _('Error(s)')
				continue_key = None if self.some_fatals else 'SPACE'
				Window.MainWindow.open_modal_window(pass_list, title=title,
					  								continue_key=continue_key, exit_key='Q')

errors = Errors()