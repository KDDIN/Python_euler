#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?
import os


Array = [2,3,5,7,11,13]
largo = 0
numprimo = 15
divisor = Array[largo]
while True:
    if len(Array) == 10001:
        print ("El numero primo numero",len(Array),"es:",Array.pop())
        os.system("pause")
        exit()

    divisor = Array[largo]
    resto = numprimo % divisor
    cociente = numprimo / divisor
    if resto == 0:
        numprimo += 2
        largo = 0

    else:
        largo += 1

    if cociente < divisor:
        Array.append(numprimo)
        numprimo += 2
        largo = 0