import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._button2)
		self._groupBox1.Controls.Add(self._button1)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(428, 154)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Select the Type of Ticket Sales"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(17, 30)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(116, 51)
		self._label1.TabIndex = 0
		self._label1.Text = "Select General Sales for all ticket sales to the general public."
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(17, 93)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(116, 53)
		self._label2.TabIndex = 1
		self._label2.Text = "Select Student Sales for all student ticket sales."
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(188, 19)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(149, 47)
		self._button1.TabIndex = 2
		self._button1.Text = "General Sales"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(188, 76)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(149, 47)
		self._button2.TabIndex = 3
		self._button2.Text = "Student Sales"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(292, 173)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(149, 47)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(453, 225)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg435TicketSalesPython"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self)
		form1.Show()
		self.Hide()

	def Button2Click(self, sender, e):
		from Form2 import *
		form2 = Form2(self)
		form2.Show()
		self.Hide()