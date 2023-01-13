#Ejercicio 6 de project euler:
#The sum of the squares of the first ten natural numbers is,
#1**2+2**2+...+10**2 = 385
#The square of the sum of the first ten natural numbers is,
#(1+2+...+10)**2 = 55**2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#3025-385 = 2640
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


numero1 = int(0)
numero2 = int(0)
suma = 1

while suma <= 100:
    numero1 += suma**2
    numero2 += suma
    if suma == 100:
        numero2 **= 2
    suma += 1

print ('el resultado del primer numero es: ',numero1)
print ('el resultado del segundo numero es: ',numero2)
print ('la diferencia entre los dos numeros es: ',numero2 - numero1)