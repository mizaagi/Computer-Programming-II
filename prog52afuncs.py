def calcArea(len, wid) -> int:
  return len * wid

def calcPerim(len: int, wid: int) -> int:
  return 2 * len + 2 * wid

def areaPerim(len, wid) -> tuple[int, int]:
  area = calcArea(len, wid)
  perim = calcPerim(len, wid)
  return area, perim

def main():
  len = int(input("Enter length: "))
  wid = int(input("Enter width: "))
  a, p = areaPerim(len, wid)
  print(f"Area: {a}\nPerimeter: {p}")
  pass


if __name__ == '__main__':
  main()
