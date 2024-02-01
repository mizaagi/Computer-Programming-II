import System.Drawing
import System.Windows.Forms
import math

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(467, 303)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 323)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(467, 131)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(492, 466)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Lang122aFor"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		self._listBox1.Items.Add("Number\tSquare\tSquare Root")
		for i in range(1, 51):
			self._listBox1.Items.Add(str(i) + "\t" + str(i**2) + "\t" + str(math.sqrt(i)))