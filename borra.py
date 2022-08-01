
import sys

a = sys.argv[1]
b = sys.argv[2]
c = len(sys.argv)

if len(sys.argv) < 4:
    d = input("D argument please:")
else:
    d = sys.argv[3]

print(a)
print(b)
print(c)
print(d)