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
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._textBox7 = System.Windows.Forms.TextBox()
		self._textBox8 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label9 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox8)
		self._groupBox1.Controls.Add(self._textBox7)
		self._groupBox1.Controls.Add(self._textBox6)
		self._groupBox1.Controls.Add(self._textBox5)
		self._groupBox1.Controls.Add(self._textBox4)
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(387, 120)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Registrant"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(7, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(45, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Name"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(229, 20)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(45, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Phone"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(7, 43)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(56, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Company"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(229, 43)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(45, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Email"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(7, 66)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(45, 23)
		self._label5.TabIndex = 4
		self._label5.Text = "Address"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(7, 89)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(45, 23)
		self._label6.TabIndex = 5
		self._label6.Text = "City"
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(126, 89)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(45, 23)
		self._label7.TabIndex = 6
		self._label7.Text = "State"
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(250, 89)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(45, 23)
		self._label8.TabIndex = 7
		self._label8.Text = "Zip"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(58, 17)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 8
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(58, 40)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 9
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(58, 63)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 10
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(31, 86)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(89, 20)
		self._textBox4.TabIndex = 11
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(270, 17)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(100, 20)
		self._textBox5.TabIndex = 12
		# 
		# textBox6
		# 
		self._textBox6.Location = System.Drawing.Point(270, 40)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(100, 20)
		self._textBox6.TabIndex = 13
		# 
		# textBox7
		# 
		self._textBox7.Location = System.Drawing.Point(156, 86)
		self._textBox7.Name = "textBox7"
		self._textBox7.Size = System.Drawing.Size(88, 20)
		self._textBox7.TabIndex = 14
		# 
		# textBox8
		# 
		self._textBox8.Location = System.Drawing.Point(270, 86)
		self._textBox8.Name = "textBox8"
		self._textBox8.Size = System.Drawing.Size(100, 20)
		self._textBox8.TabIndex = 15
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(1, 190)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(120, 38)
		self._button1.TabIndex = 1
		self._button1.Text = "&Select Conference Options"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(139, 190)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(120, 38)
		self._button2.TabIndex = 2
		self._button2.Text = "&Reset"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(280, 190)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(120, 38)
		self._button3.TabIndex = 3
		self._button3.Text = "E&xit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# label9
		# 
		self._label9.Location = System.Drawing.Point(187, 153)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 4
		self._label9.Text = "Total Cost:"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(406, 230)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg479ConferenceRegistration"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)

