# Cl213f.py
class Cl213f:
    def __init__(self, kwh):
        self.kwh = kwh
        self.cost = 0.0

    def calc(self):
      for i in range(self.kwh):
        if i <= 2000:
          self.cost += 0.07
        if i > 2000 and i <= 10_000:
          self.cost += 0.05
        if i > 10_000:
          self.cost += 4
      return self.cost

    def __str__(self):
        return f"The cost of {self.kwh} is {self.calc()}"
