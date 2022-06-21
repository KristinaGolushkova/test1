a = int(input("введите сторону треугольника : "))

b = int(input("введите вторую сторону треугольника : "))
# g
c = int(input("введите третью сторону треугольника : "))

from math import sqrt
print("Площадь треугольника :")
p = .5*(a+b+c)
S = sqrt(p*(p - a)*(p - b)*(p - c))


print(S)
