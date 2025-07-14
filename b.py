import math


a = 1
b = -3
c = 2

D = b**2 - 4*a*c


if D < 0:
    print("No real roots.")
elif D == 0:
    x = -b / (2*a)
    print("One real root:", x)
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Two real roots:", x1, x2)


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print(f"Roots are: {root1}, {root2}")
else:
    print("No real roots.")
