import subprocess
import math
import Tkinter
from Tkinter import *


class Gsettings(list):
	def __init__(self, key):
		if not(isinstance(key, basestring)):
			raise TypeError
		self.key = key
		self.value = self.getSettings()

	def getSettings(self):
		bashCommand = "gsettings get org.pantheon.terminal.settings {}".format(self.key)

		output= subprocess.check_output(['bash','-c', bashCommand])
		return output.replace("\n", "").replace("\"","").replace("'", "").split (':')

	def setSettings(self, value):	
		bashCommand = "gsettings set org.pantheon.terminal.settings {} {}".format(self.key, value)

class Palette( Gsettings):
	#Backend
	def __init__(self):
		super(Palette, self ).__init__('palette')
		self.palette = self.getSettings()
                self.value = self.getSettings()
		print self.palette

	def getPalette(self):
		return self.getSettings()
	def setPalette(self, id_color_to_change, color):
		self.palette[id_color_to_change] = color
		p = "'"+":".join(self.palette)+"'"
		print id_color_to_change
		bashCommand = "gsettings set org.pantheon.terminal.settings palette {}".format(p)
		output= subprocess.check_output(['bash','-c', bashCommand])
                self.value = self.getSettings()
	def __len__(self):
		print len(self.palette)
		print self.palette
		return len(self.palette)
