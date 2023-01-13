#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

Array = []

def FactorPrimo (numero):
    factorPrimo = 2

    while numero > 1:
        resto = numero % factorPrimo
        if resto == 0:
            Array.append(factorPrimo)
            numero /= factorPrimo
        else:
            factorPrimo += 1

    print (Array)
    print("el factor primo mas largo es: ",Array.pop())

FactorPrimo (600851475143)