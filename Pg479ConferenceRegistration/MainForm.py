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
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
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
		self._groupBox1.Size = System.Drawing.Size(519, 162)
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
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(544, 376)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg479ConferenceRegistration"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)

