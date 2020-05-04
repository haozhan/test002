from math import sqrt
import sys

print("The command line arguments are:")
for i in sys.argv:
    print(i)

print("\n\nThe PYTHONPATH is", sys.path, "\n")

print("Square root of 16 is ", sqrt(16))


if __name__ == "__main__":
    print("This programs is being run by itself.")
else:
    print("I am being imported from another module.")
