class ItemSales:
	def __init__(self, quan=0, price=0, total=0):
		self.quan = quan
		self.price = price
		self.total = total
		
	def get_quan(self):
		self.quan = int(input("Enter quantity: "))
		
	def calc_price(self):
		if 0 < self.quan < 100:
			self.price = 5.95
		elif 99 < self.quan < 200:
			self.price = 5.75
		elif 199 < self.quan < 300:
			self.price = 5.40
		elif 299 < self.quan:
			self.price = 5.15
			
	def show_total(self):
		self.total = self.quan * self.price
		print(f"Total Price: ${self.total}")

def main():
	NewItemSales = ItemSales()
	NewItemSales.get_quan()
	NewItemSales.calc_price()
	NewItemSales.show_total()

if __name__ == "__main__":
	main()