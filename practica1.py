from Crypto.Util import number
import random

#Ejercicio 1
#Obtener numero aleatorio de 256 bits
print("Ejercicio 1 - Obtener numero de 256 bits usando la funcion random", random.getrandbits(256), "\n")

#Ejercicio 2
i = 0
while(True):
    i = i+1
    j = random.getrandbits(1024)
    isPrime = number.isPrime(j)
    if (isPrime):
        print("En la iteración: ", i, " se encontró el primo: ", j, "\n")
        break

#Ejercicio 3
#Obtener inverso multiplicativo
def inversoMultiplicativo(x,y):
    print("Ejercicio 3 - El inverso multiplicativo del numero x:", "\n", x, "\n","y el numero y: ", "\n", y, "\n", number.inverse(x,y), "\n")

a = random.getrandbits(1024)
b = random.getrandbits(1024)
inversoMultiplicativo(a,b)

#Ejercicio 4
#Potencia de un numero 2^(mod) p, donde "e" es un numero de 256 bits y "p" es un primo de 1024 bits
x = 2
y = random.getrandbits(256)
z = j

def potencia( x, y, z):
    print("Ejercicio 4 - la potencia de x a la y mod z es: ", pow(x, y ,z), "\n")

potencia(x,y,z)


