#Acceso por medio de índice en string
Fruta = 'manzana' #Fruta = ['m', 'a', 'n', 'z'...]
letra = Fruta[5]
print(letra)

print("El While")

#Uso de iteración con string
indice = 0
while indice < len(Fruta):
    letra = Fruta[indice]
    print(letra)
    indice = indice + 1 # indice++ | indice += 1

print("El for")
for i in range(len(Fruta)):
    print(Fruta[i])

#Impresión segmentada
Frase = 'Monty Python'
print(Frase[0:5])
#Salida: Monty
print(Frase[3:12])
#Salida: Python
print(Frase[3:])
#Salida: ty Python
print(Frase[:4])
#Salida: Mont

