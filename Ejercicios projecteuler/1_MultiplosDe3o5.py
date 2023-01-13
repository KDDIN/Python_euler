#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def tabla(multiplicador):
    
    resultado = 0    
    for numero in range(1000):
        multiplicacion = numero * multiplicador
        if multiplicacion < 1000:
            resultado = resultado + multiplicacion
        else:
            return resultado
            
print (tabla(3) + tabla(5))


