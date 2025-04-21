import math
x= -10
y= 5

print("Absolute of x:", abs(x))
print("Absolute of y:", abs(y))

print("Add:", x+y)
print("Sub:", x-y)
print("Mul:", x*y)
print("Div:", x/y)
print("pow:", x**y)

print("Bitwise OR:", x|y)
print("Bitwise AND:", x&y)
print("Bitwise XOR:", x^y)

print("Fac of y:", math.factorial(y))

if x >= 0:
    print("Fac of x:", math.factorial(x))
else:
     print("Fac of x: Error(cannot compute factorial of negative number)")