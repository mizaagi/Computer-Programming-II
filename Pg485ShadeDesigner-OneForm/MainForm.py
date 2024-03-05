import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._label5 = System.Windows.Forms.Label()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Regular shades ($0)",
			"Folding shades ($10)",
			"Roman shades ($15)"]))
		self._comboBox1.Location = System.Drawing.Point(56, 37)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 190)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(159, 24)
		self._label1.TabIndex = 1
		self._label1.Text = "TOTAL:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 13)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(153, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Base Fee - $50"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(12, 40)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(38, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Styles:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(12, 78)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(38, 23)
		self._label4.TabIndex = 4
		self._label4.Text = "Sizes:"
		# 
		# comboBox2
		# 
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["25 inches wide ($0)",
			"27 inches wide ($2)",
			"32 inches wide ($4)",
			"40 inches wide ($6)"]))
		self._comboBox2.Location = System.Drawing.Point(56, 75)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(121, 21)
		self._comboBox2.TabIndex = 5
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(12, 116)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(46, 23)
		self._label5.TabIndex = 6
		self._label5.Text = "Colors:"
		# 
		# comboBox3
		# 
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["Natural ($5)",
			"Blue ($0)",
			"Teal ($0)",
			"Red ($0)",
			"Green ($0)"]))
		self._comboBox3.Location = System.Drawing.Point(56, 113)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(121, 21)
		self._comboBox3.TabIndex = 7
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 143)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(164, 44)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(183, 207)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._comboBox3)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._comboBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._comboBox1)
		self.Name = "MainForm"
		self.Text = "Design Your Own Window Shade"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		total = 50.0
		if self._comboBox1.SelectedItem == "Folding shades ($10)":
			total += 10.0
		elif self._comboBox.SelectedItem == "Roman shades ($15)":
			total += 15.0
		if self._comboBox2.SelectedItem == "27 inches wide ($2)":
			total += 2.0
		elif self._comboBox2.SelectedItem == "32 inches wide ($4)":
			total += 4.0
		elif self._comboBox2.SelectedItem == "40 inches wide ($6)":
			total += 6.0
		if self._comboBox3.SelectedItem == "Natural ($5)":
			total += 5.0
		self._label1.Text = "TOTAL: $" + str(total)
			