#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
def ValidarPalindromo (numero):
    numeroinverso = int(str(numero)[::-1])
    if numero == numeroinverso:        
        return True
    else:        
        return False
        
numero1 = int(900)
numero2 = int(900)
Array = []

while numero1 < 1000:
    if numero2 == 1000:
        numero2 = 900
        numero1 += 1

    resultado = int(numero1 * numero2)
    numero2 += 1
    if ValidarPalindromo(resultado) == True:
        Array.append(int(resultado))

print(Array)
print("el palindromo mas grande es: ",Array.pop())
