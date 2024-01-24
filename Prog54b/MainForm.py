import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(535, 140)
		self._label1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 321)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(535, 79)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(13, 164)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(535, 140)
		self._label2.TabIndex = 2
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(560, 403)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		num1 = 475
		num2 = 821
		num3 = 369
		num4 = 562
		sum = num1+num2+num3+num4
		avg = sum / 4
		self._label1.Text = "Average: " + str(avg)
		self._label2.Text = "Sum: " + str(sum)