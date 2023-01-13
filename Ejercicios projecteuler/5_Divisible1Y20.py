#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def Aumento (numero):
    divisor = 1
    resto = numero
    while divisor <= 20:    
        resto %= divisor
        if resto != 0:
            return False

        divisor += 1
        resto = numero

    return True

pase = True
numeroaumento = 20

while pase == True:
    if Aumento(numeroaumento) == True:
        print(numeroaumento," es el menor numero que es divisible entre 1 y 20, dando 0 en el resto de todas las divisiones")
        pase = False
    else:
        numeroaumento += 1