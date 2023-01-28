#Comentarios de una Linea
'''Comentarios
de
mas de
una Linea'''

#Tipos de Variable

a = 999999              #Variable tipo int
caracter1 = "a"
caracter2 = "a"
b = "dos"               #Variable Tipo String
c = 25.007              #Variable tipo float
d = True                #Variable tipo booleana verdadera
e = False               #Variable tipo booleana falsa
f = [a,b,c,d,e,"Holi"]  #Variable tipo Lista

#Sentencia para imprimir
print("Hola mundo "+ str(int("12")+int(6)))

#Type sirve para devolver que tipo de dato es la variable
print(type(1))
print(type(f))
if type(a)==type(c):
    print("iguales")
else:
    print("no iguales")

#Imprimir los tipos de variable y su valor
print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(d),d)
print(type(e),e)
print(type(f),f)

#Casteo de Variables
print(ord("a"))
letra = "H"
if ord(letra) >= 97 and ord(letra) <= 122:
    print("letra minuscula")
else:
    print("Letra Mayúscula")

#Palabras Reservadas
"""and
as
assert
break
class
continue
def
"""

#Operaciones en python
a= 1
print(a+58)                 #Suma
print(a-3)                  #Resta
print(a*15)                 #Multiplicacion
a=59
print(a/6)                 #Division
print("Division Truncada",a//60)                 
print("Division Truncada con casteo",a//60)                 
a = 2
b = 3
print(a**b)                 #Potencia
print(8%2)                  #Modular

