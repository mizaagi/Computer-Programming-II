import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 226)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(103, 226)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(197, 226)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(95, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(177, 20)
		self._textBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(75, 17)
		self._label1.TabIndex = 4
		self._label1.Text = "Radius:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(13, 86)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(259, 35)
		self._label2.TabIndex = 5
		self._label2.Text = "Area:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(13, 143)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(259, 35)
		self._label3.TabIndex = 6
		self._label3.Text = "Circumference:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightGreen
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pi = 3.14
		area = 0
		circumference = 0
		area = pi * int(self._textBox1.Text)**2
		circumference = 2 * pi * int(self._textBox1.Text)
		self._label2.Text = "Area: " + str(area)
		self._label3.Text = "Circumference: " + str(circumference)