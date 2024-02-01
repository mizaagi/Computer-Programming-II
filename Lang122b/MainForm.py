import System.Drawing
import System.Windows.Forms

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
		self._listBox1.Size = System.Drawing.Size(414, 277)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(123, 297)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(175, 57)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(439, 366)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Lang122b"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		self._listBox1.Items.Add("Hours\tPay")
		for i in range(1, 41):
			self._listBox1.Items.Add(str(i) + "\t" + str(i*4))