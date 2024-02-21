import sys


def main(args):
  print("Sum:", sum(int(args[0]), int(args[1])))


if __name__ == "__main__":
  main(sys.argv[1:])