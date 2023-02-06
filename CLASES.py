class complejo:
    Real = 0

    #Constructor
    def __init__(self,ParteReal,ParteImaginaria):
        self.Real = ParteReal                       #Self puede crear la variable dentro del constructor
        self.Imaginaria = ParteImaginaria
    def NumeroString(self):
        return "" + str(self.Real) + " " + str(self.Imaginaria) + "i"

    def suma(self,ParteReal,ParteImaginaria):
        self.Real = self.Real + float(ParteReal)
        self.Imaginaria = self.Imaginaria + float(ParteImaginaria)


y = complejo(2.5,10)
print(y.Real)
print(y.NumeroString())
y.suma('55',0.6)
print(y.NumeroString())

class Perro:

    Tipo = 'Canino'
    
    def __init__(self,nombre):
        self.nombre = nombre
        self.__trucos = []      #Atributo privado
    
    def AgregarTruco(self,Truco):
        self.__trucos.append(str(Truco))
    
    def MostrarTrucos(self):
        for truco in self.__trucos:
            print(self.nombre,"hace",truco)

    def DevolverTrucos(self):
        return self.__trucos 

n = Perro('Dory') #Objeto 1  
x = Perro('Peque') #Objeto 2
print('-------------------------------------')
print('Tipo Animal:',n.Tipo,'\nNombre:',n.nombre)
print('-------------------------------------')
print('Tipo Animal:',x.Tipo,'\nNombre:',x.nombre)

#Cambiar atributos sin método
print('---------------CAMBIO DE ATRIBUTO-------------------')
n.Tipo = 'French'
x.Tipo = 'Poodle'

print('-------------------------------------')
print('Tipo Animal:',n.Tipo,'\nNombre:',n.nombre)
print('-------------------------------------')
print('Tipo Animal:',x.Tipo,'\nNombre:',x.nombre)

#Atributos privados
print("---------------------Uso de atributos privados---------------------")
n.AgregarTruco("Dar la pata")
n.AgregarTruco("Hacerse el morido")

n.MostrarTrucos()

x.AgregarTruco("Saltar en un aro")
x.AgregarTruco("Comer cereal con cuchara")

print("------------------------------------------")
print("Trucos de ", x.nombre)
for truco in x.DevolverTrucos():
    print(truco)
print("------------------------------------------")