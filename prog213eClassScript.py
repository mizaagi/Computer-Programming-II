class Prog213e:
	def __init__(self, numsList=[], dist=[0,0,0,0,0], perc=[0,0,0,0,0]):
		self.numsList = numsList
		self.dist = dist
		self.perc = perc
		
	def readFile(self):
		try:
			with open("Langdat/prog213e.dat", 'r') as f:
				for line in f:
					self.numsList.append(int(line))
		except Exception as e:
			print("Error:", e)
		pass
		
	def getInfo(self):
		for n in self.numsList:
			if n < 20:
				self.dist[0] = self.dist[0] + 1
			elif 20 <= n < 40:
				self.dist[1] = self.dist[1] + 1
			elif 40 <= n < 60:
				self.dist[2] = self.dist[2] + 1
			elif 60 <= n < 80:
				self.dist[3] = self.dist[3] + 1
			elif 80 <= n:
				self.dist[4] = self.dist[4] + 1
		_total = sum(self.dist)
		for i in range(0, 5):
			self.perc[i] = round((self.dist[i] / _total) * 10, 2)

	def showTable(self):
		print("-----------------Langner Family-----------------")
		print("Age Group\tDistribution\tPercentage")
		print(f"<20\t\t\t{self.dist[0]}\t\t\t\t{self.perc[0]}")
		print(f"20-39\t\t{self.dist[1]}\t\t\t\t{self.perc[1]}")
		print(f"40-59\t\t{self.dist[2]}\t\t\t\t{self.perc[2]}")
		print(f"60-79\t\t{self.dist[3]}\t\t\t\t{self.perc[3]}")
		print(f">79\t\t\t{self.dist[4]}\t\t\t\t{self.perc[4]}")
		print("------------------------------------------------")




def main():
	prog = Prog213e()
	prog.readFile()
	prog.getInfo()
	prog.showTable()


if __name__ == "__main__":
	main()