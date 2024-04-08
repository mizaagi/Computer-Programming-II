class lp3_11():
  def __init__(self):
    self._design = 0
    self._code = 0
    self._debug = 0
    self._test = 0
  
  def get_times(self):
    self._design = int(input("Designing time (m): "))
    self._code = int(input("Coding time (m): "))
    self._debug = int(input("Debugging time (m): "))
    self._test = int(input("Testing time (m): "))
  
  def calc(self):
    total = self._design + self._code + self._debug + self._test
    desTime = round((100 * self._design / total), 2)
    codTime = round((100 * self._code / total), 2)
    debTime = round((100 * self._debug / total), 2)
    tesTime = round((100 * self._test / total), 2)
    print(f"Task\t\t% of Time\nDesigning\t{desTime}%\nCoding\t\t{codTime}%\
            \nDebugging\t{debTime}%\nTesting\t\t{tesTime}%")


instance = lp3_11()
instance.get_times()
instance.calc()