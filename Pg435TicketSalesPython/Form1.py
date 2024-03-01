
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.parent = parent
		self._decTAXRATE = 0.06
		
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._txtNumTickets = System.Windows.Forms.TextBox()
		self._radSectionA = System.Windows.Forms.RadioButton()
		self._radSectionB = System.Windows.Forms.RadioButton()
		self._radSectionC = System.Windows.Forms.RadioButton()
		self._lblTickets = System.Windows.Forms.Label()
		self._lblTax = System.Windows.Forms.Label()
		self._lblTotal = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._txtNumTickets)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(449, 99)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "How Many Tickets?"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radSectionC)
		self._groupBox2.Controls.Add(self._radSectionB)
		self._groupBox2.Controls.Add(self._radSectionA)
		self._groupBox2.Location = System.Drawing.Point(13, 119)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(222, 158)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Section"
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._lblTotal)
		self._groupBox3.Controls.Add(self._lblTax)
		self._groupBox3.Controls.Add(self._lblTickets)
		self._groupBox3.Location = System.Drawing.Point(241, 119)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(223, 158)
		self._groupBox3.TabIndex = 2
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Total Cost"
		# 
		# btnCalculate
		# 
		self._btnCalculate.Location = System.Drawing.Point(52, 284)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(141, 37)
		self._btnCalculate.TabIndex = 3
		self._btnCalculate.Text = "Calcula&te"
		self._btnCalculate.UseVisualStyleBackColor = True
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(286, 283)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(141, 37)
		self._btnClose.TabIndex = 4
		self._btnClose.Text = "&Close"
		self._btnClose.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(228, 65)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Number of tickets:"
		# 
		# txtNumTickets
		# 
		self._txtNumTickets.Location = System.Drawing.Point(334, 62)
		self._txtNumTickets.Name = "txtNumTickets"
		self._txtNumTickets.Size = System.Drawing.Size(100, 20)
		self._txtNumTickets.TabIndex = 1
		# 
		# radSectionA
		# 
		self._radSectionA.Location = System.Drawing.Point(7, 20)
		self._radSectionA.Name = "radSectionA"
		self._radSectionA.Size = System.Drawing.Size(104, 24)
		self._radSectionA.TabIndex = 0
		self._radSectionA.TabStop = True
		self._radSectionA.Text = "Section A"
		self._radSectionA.UseVisualStyleBackColor = True
		# 
		# radSectionB
		# 
		self._radSectionB.Location = System.Drawing.Point(6, 70)
		self._radSectionB.Name = "radSectionB"
		self._radSectionB.Size = System.Drawing.Size(104, 24)
		self._radSectionB.TabIndex = 2
		self._radSectionB.TabStop = True
		self._radSectionB.Text = "Section B"
		self._radSectionB.UseVisualStyleBackColor = True
		# 
		# radSectionC
		# 
		self._radSectionC.Location = System.Drawing.Point(7, 121)
		self._radSectionC.Name = "radSectionC"
		self._radSectionC.Size = System.Drawing.Size(104, 24)
		self._radSectionC.TabIndex = 3
		self._radSectionC.TabStop = True
		self._radSectionC.Text = "Section C"
		self._radSectionC.UseVisualStyleBackColor = True
		# 
		# lblTickets
		# 
		self._lblTickets.Location = System.Drawing.Point(57, 26)
		self._lblTickets.Name = "lblTickets"
		self._lblTickets.Size = System.Drawing.Size(149, 23)
		self._lblTickets.TabIndex = 0
		self._lblTickets.Text = "Ticket Cost:"
		# 
		# lblTax
		# 
		self._lblTax.Location = System.Drawing.Point(57, 76)
		self._lblTax.Name = "lblTax"
		self._lblTax.Size = System.Drawing.Size(149, 23)
		self._lblTax.TabIndex = 1
		self._lblTax.Text = "Tax:"
		# 
		# lblTotal
		# 
		self._lblTotal.Location = System.Drawing.Point(57, 123)
		self._lblTotal.Name = "lblTotal"
		self._lblTotal.Size = System.Drawing.Size(149, 23)
		self._lblTotal.TabIndex = 2
		self._lblTotal.Text = "Total:"
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(474, 326)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form1"
		self.Text = "Form1"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
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

	def BtnCalculateClick(self, sender, e):
		intNumTickets = 0
		decTicketCost = 0.0
		decTotal = 0.0
		
		intNumTickets = int(self._txtNumTickets.Text)
		decTicketCost = intNumTickets * self.PriceEachTicket()
		decSalesTax = self.CalcTax(decTicketCost)
		decTotal = decTicketCost + decSalesTax
		
		self._lblTickets.Text = "Ticket Cost: " + str(decTicketCost)
		self._lblTax.Text = "Tax: " + str(decSalesTax)
		self._lblTotal.Text = "Total: " + str(decTotal)