import math
from math import pi

class Prog54c():
  def __init__(self, rad, area=0, circum=0):
    self.rad = rad
    self.area = area
    self.circum = circum
  def calc(self):
    self.area = pi * (self.rad ** 2)
    self.circum = 2 * pi * self.rad
  def show_area(self):
    print(f"Area: {self.area}")
  def show_circum(self):
    print(f"Circumference: {self.circum}")


circle = Prog54c(int(input("Radius: ")))
circle.calc()
circle.show_area()
circle.show_circum()