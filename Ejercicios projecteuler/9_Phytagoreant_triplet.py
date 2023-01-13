import os
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a**2 + b**2 = c**2
#For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#30**2 = 900
a = 1
b = 2
resultado = 0

while resultado != 1000:
    b += 1
    if b == 400:
        a += 1
        b = a + 1
    else:
        c2 = a**2 + b**2
        c = pow(c2, 0.5)
        resultado = a + b + c


print(a,"+",b,"+",c,"=",resultado)
print("El producto de estos 3 numeros es:", a,"x",b,"x",c,"=",a*b*c)


