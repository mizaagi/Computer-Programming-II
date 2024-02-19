class Shape:
  def __init__(self, len, wid):
    self.len = len
    self.wid = wid
    self._area = 0
    self._perim = 0
  
  def calculate(self):
    self._area = self.len * self.wid
    self._perim = 2 * self.len + 2 * self.wid

  def setLength(self, length):
    self.len = length
  
  def getArea(self):
    return self._area

  def getPerim(self):
    return self._perim



def main():
  len = int(input("Enter length: "))
  wid = int(input("Enter width:  "))
  shape = Shape(len, wid)
  shape.calculate()
  print("Perimeter:", shape.getPerim())
  print("Area:", shape.getArea())
  pass


if __name__ == "__main__":
  main()