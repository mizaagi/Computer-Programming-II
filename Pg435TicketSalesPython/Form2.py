
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
	def __init__(self, parent):
		self._decTAXRATE = 0.06
		self.parent = parent
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(292, 162)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "How Many Tickets?"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._label3)
		self._groupBox2.Controls.Add(self._label2)
		self._groupBox2.Controls.Add(self._label1)
		self._groupBox2.Location = System.Drawing.Point(311, 13)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(142, 162)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Total Cost"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(7, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Ticket Cost:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(7, 72)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Tax:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(7, 130)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Total:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(20, 19)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 0
		self._label4.Text = "Number of Tickets:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(126, 16)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(20, 72)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(252, 32)
		self._label5.TabIndex = 2
		self._label5.Text = "Student tickets are for seating in the student section only."
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(243, 207)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 2
		self._button1.Text = "Calcula&te"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(343, 207)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 3
		self._button2.Text = "&Close"
		self._button2.UseVisualStyleBackColor = True
		# 
		# Form2
		# 
		self.ClientSize = System.Drawing.Size(465, 260)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form2"
		self.Text = "Form2"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)
		
	def PriceEachTicket(self):
		if self._radSectionA.Checked:
			return 20
		elif self._radSectionB.Checked:
			return 15
		elif self._radSectionC.Checked:
			return 10
		
	def CalcTax(self, cost):
		return cost * self._decTAXRATE

	def Button1Click(self, sender, e):
		intNumTickets = 0
		decTicketCost = 0.0
		decTotal = 0.0
		
		intNumTickets = int(self._textBox1.Text)
		decTicketCost = intNumTickets * 7 # Student Price
		decSalesTax = self.CalcTax(decTicketCost)
		decTotal = decTicketCost + decSalesTax
		
		self._label1.Text = "Tickets: " + str(decTicketCost)
		self._label2.Text = "Tax: " + str(decSalesTax)
		self._label3.Text = "Total: " + str(decTotal)