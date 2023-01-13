def multiplicararray (array): #este metodo va obteniendo los datos de un array y los va multiplicando
    multiplicacion = 1 #esta varaible la uso para multiplicar a los numeros
    for numero in array:  #voy recorriendo el array espacio por espacio
        multiplicacion *= numero #tomo un numero del array, lo multiplico por 1, el resultado se guarda en la var multiplicacion y sigue multiplicando
        #sucesivamente hasta recorrer todo el array

    return multiplicacion #retorna el numero final, ya multiplicado

numero = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
arreglocontenedor = [int(a) for a in str(numero)] #este arreglo sirve para separar a todos los numeros y ponerlos en un solo arreglo.
#para esto, creo la variable a, la cual la asigno como int, y hago que esta recorra toda la variable numero, cambiando el tipo de numero a 
#str para evitar errores, va progresivamente pasando los numeros a el arreglo individualmente
arreglocomparador = [] #este arreglo lo voy a usar para multiplicar los numeros
arreglofinal = [] #este arreglo lo voy a usar para guardar todos los numeros multiplicados
largo = 0 #esta variable la voy a utilizar para obtener un numero base del arreglo
multiplicador = arreglocontenedor[largo] #en esta variable se guardan los numeros del array
limite = 0 #el limite sirve para ir obteniendo otros numeros en el array
while largo != 988: #esta condicion sirve para que no se sobrepase al array y de errores
    if limite == 13: #si el limite da 13, se reinicia, aumenta el largo, agragan los datos en el arrayfinal y reinicia los datos del comparador
        limite = 0
        largo += 1
        arreglofinal.append(multiplicararray(arreglocomparador))
        arreglocomparador = []

    else:#sino le ingresa los datos al array comparador y aumenta el limite
        arreglocomparador.append(arreglocontenedor[largo + limite])
        limite +=1

print("el numero max es: ",max(arreglofinal))

if True:
    print ("hola")
    
    
    