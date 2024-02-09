import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(13, 13)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "daytime"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(124, 12)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "evening"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(235, 13)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "off-peak"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(108, 57)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 60)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 4
		self._label1.Text = "minutes"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 108)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 5
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 175)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 6
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(591, 400)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Name = "MainForm"
		self.Text = "Prog272LongDistance"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		if self._radioButton1.Checked:
			self._label2.Text == str(