# Proyecto conversor de moneda basico de COP A USD o viceversa

print("")
print("Bienvenido al primer conversor de moneda oficial de lucarova7")
print("")
print("Opcion [1]: Pesos colombianos a Dolares COP-USD ")
print("")
print("Opcion [2]: Dolares a Pesos Colombianos USD-COP ")

# Valor del dolar tomado el dia 29 de Abril de 2022

Valor_Dolar = float(3956)

print("")
Opcion = input("Elige el numero de la opcion que deseas: ")

#Pesos Colombianos a Dolares USD

if Opcion == "1":
    print("")
    Pesos = float(input("Ingrese la cantidad de pesos colombianos que desea convertir: "))
    USD = round(Pesos / Valor_Dolar, 2)
    Pesos = round(Pesos, 2)
    Pesos = str(Pesos)
    USD = str(USD)
    print("")
    print("$" + Pesos + " COP Equivalen a $" + USD + " Dolares")

# Dolares a Pesos Colombianos

elif Opcion == "2":
    print("")
    Dolares = float(input("Ingrese la cantidad de dolares que desea convertir: "))
    COP = round(Dolares * Valor_Dolar, 2)
    Dolares = round(Dolares, 2)
    Dolares = str(Dolares)
    COP = str(COP)
    print("")
    print("$" + Dolares + " USD Equivalen a $" + COP + " Pesos Colombianos")

else:
    print("")
    print("Start Again Danny")

# Fin primera version


