



import re

import jk_terminal_essentials







class SimpleTextLineOutputBuffer(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self):
		self.lines = []
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def height(self) -> int:
		return len(self.lines)
	#

	@property
	def width(self) -> int:
		if self.lines:
			return max([
				len(line) for line in self.lines
			])
		else:
			return 0
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def print(self, s:str = None):
		if s is None:
			self.lines.append("")
			return
		else:
			s = str(s)

		s = jk_terminal_essentials.stripColors(s)
		m = re.match("^(\t+)", s)
		if m:
			n = len(m.group(1))
			s = (" " * 8 * n) + s[n:]
		s = s.replace("\t", "    ")
		self.lines.append(s)
	#

	def get(self, rowNo:int) -> str:
		if 0 <= rowNo < len(self.lines):
			return self.lines[rowNo]
		else:
			return ""
	#

#














