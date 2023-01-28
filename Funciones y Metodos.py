#Funciones Nativas
lista = [1,2,3,4,6]
numero = 9999

#Para ver el tamaño de lista
print(len(lista))

#Para Agregar a la lista
lista.append(1)
print(len(lista))


#Funciones Importadas
import random
print("Qué es random?",random.random())                 #Muestra un numero aleatorio menor a 1
for i in range(10):                                     #Imprime 10 numeros aleatorios
    x = random.random()
    print(x)

#Creacion de Método (no retorno)
def No_Repito(numero):
    print("No repito dos veces")
    if(int(numero) % 2 == 0):
        print("Que dijo?")

No_Repito(int(random.random()*10))

#Creacion de función con retorno
def Suma_De_Tres(num1,num2,num3):
    if num1 > 2:
        return str(num1+num2+num3)
    elif num1 == 3:
        return 10
    else:
        return True

print(Suma_De_Tres(6,2,3),type(Suma_De_Tres(6,2,3)))