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
		self._btnGeneral = System.Windows.Forms.Button()
		self._btnStudent = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._btnStudent)
		self._groupBox1.Controls.Add(self._btnGeneral)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(389, 165)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Select the Type of Ticket Sales"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(30, 48)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(166, 31)
		self._label1.TabIndex = 0
		self._label1.Text = "Select General Sales for all ticket sales to the general public."
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(30, 111)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(166, 31)
		self._label2.TabIndex = 1
		self._label2.Text = "Select Student Sales for all student ticket sales."
		# 
		# btnGeneral
		# 
		self._btnGeneral.Location = System.Drawing.Point(217, 29)
		self._btnGeneral.Name = "btnGeneral"
		self._btnGeneral.Size = System.Drawing.Size(93, 50)
		self._btnGeneral.TabIndex = 2
		self._btnGeneral.Text = "&General Sales"
		self._btnGeneral.UseVisualStyleBackColor = True
		self._btnGeneral.Click += self.BtnGeneralClick
		# 
		# btnStudent
		# 
		self._btnStudent.Location = System.Drawing.Point(217, 92)
		self._btnStudent.Name = "btnStudent"
		self._btnStudent.Size = System.Drawing.Size(93, 50)
		self._btnStudent.TabIndex = 3
		self._btnStudent.Text = "&Student Sales"
		self._btnStudent.UseVisualStyleBackColor = True
		# 
		# btnExit
		# 
		self._btnExit.Location = System.Drawing.Point(309, 193)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(93, 31)
		self._btnExit.TabIndex = 4
		self._btnExit.Text = "E&xit"
		self._btnExit.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(414, 236)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "University Concert Hall"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def BtnGeneralClick(self, sender, e):
		from frmGeneral import *
		frmGeneral = 