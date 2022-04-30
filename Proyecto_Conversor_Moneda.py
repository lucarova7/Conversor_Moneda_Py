# Proyecto conversor de moneda basico de Pesos Colombianos

Menu = """
Bienvenido al primer conversor de moneda oficial de lucarova7

Opcion [1]: Pesos colombianos a Dolares COP-USD
Opcion [2]: Dolares a Pesos Colombianos USD-COP
Opcion [3]: Pesos Colombianos a Euros COP-€
Opcion [4]: Euros a Pesos Colombianos €-COP

Elige el numero de la opcion que deseas: 
"""

# Valores tomados el dia 29 de Abril de 2022

Valor_Dolar = float(3956)
Valor_Euro = float(4174)

Opcion = input(Menu)

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

# Dolares a Pesos Colombianos COP

elif Opcion == "2":
    print("")
    Dolares = float(input("Ingrese la cantidad de dolares que desea convertir: "))
    COP = round(Dolares * Valor_Dolar, 2)
    Dolares = round(Dolares, 2)
    Dolares = str(Dolares)
    COP = str(COP)
    print("")
    print("$" + Dolares + " USD Equivalen a $" + COP + " Pesos Colombianos")

#Pesos Colombianos a Euros €

elif Opcion == "3":
    print("")
    Pesos = float(input("Ingrese la cantidad de pesos colombianos que desea convertir: "))
    Euros = round(Pesos / Valor_Euro, 2)
    Pesos = round(Pesos, 2)
    Pesos = str(Pesos)
    Euros = str(Euros)
    print("")
    print("$" + Pesos + " COP Equivalen a $" + Euros + " Euros")

#Euros a pesos Colombianos COP

elif Opcion == "4":
    print("")
    Euros = float(input("Ingrese la cantidad de euros que desea convertir: "))
    Pesos_COP = round(Euros * Valor_Euro, 2)
    Euros = round(Euros, 2)
    Euros = str(Euros)
    Pesos_COP = str(Pesos_COP)
    print("")
    print("$" + Euros + " € Equivalen a $" + Pesos_COP + " Pesos Colombianos")

else:
    print("")
    print("Start Again Danny")

# Segunda version


