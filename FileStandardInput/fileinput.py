__name__ = 'FileInput'
__author__ = 'Ashik Vetrivelu <ashik@cepheuen.com>'
class input(object):
	def __init__(self, filename):
		super(input, self).__init__()
		self.filename = filename
		file = open(filename,'r')
		self.lines = file.read().splitlines()
		file.close()
		self.lines.reverse()
	def file_input(self):
		output = self.lines.pop()
		return output
