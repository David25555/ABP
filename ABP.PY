#Pas 1: Importarem el csv en el programa.

import csv

#Pas 2: Crearem una funciió que carregui les dades del arxiu csv.
def carregar_dades(nom_fitxer):
    dades = []
    with open(nom_fitxer, mode='r', encoding='utf-8') as fitxer:
        lector = csv.DictReader(fitxer)
        for fila in lector:
            fila['Quantitat_Venuda'] = int(fila['Quantitat_Venuda'])
            fila['Preu_Unitari'] = float(fila['Preu_Unitari'])
            fila['IVA'] = float(fila['IVA'])
            fila['Estoc_Disponible'] = int(fila['Estoc_Disponible'])
            dades.append(fila)
    return dades

#Pas 3: Crearem una funció que calculi la facturació del mes

def calculFactMes():
    arxiu = "dades_botiga.csv"
    dades = carregar_dades(arxiu)
    total_sense_iva = 0
    total_amb_iva = 0
    for fila in dades:
        subtotal = fila["Quantitat_Venuda"] * fila["Preu_Unitari"]
        iva = (fila["IVA"]/100)
        total_sense_iva += subtotal
        total_amb_iva += subtotal+iva

    print("Facturació amb IVA:", total_amb_iva)
    print("Facturació sense IVA:", total_sense_iva)
 

#Crearem una altré funció que el que fa sera calcular el stock
def calcul_stock ():
    arxiu = "dades_botiga.csv"
    dades = carregar_dades(arxiu)
    print("ESTOC DISPONIBLE PER PRODUCTE")
    for fila in dades:
        print(fila["Producte"], ": ", fila["Estoc_Disponible"])
        
  

#Crearem una altré funció que calculi els productes mes facturats
def productes_mes_facturats():
    arxiu = "dades_botiga.csv"
    dades = carregar_dades(arxiu)
    
    gran1 = 0
    gran2 = 0
    gran3 = 0

    total_amb_iva = 0
    for fila in dades:
        subtotal = fila["Quantitat_Venuda"] * fila["Preu_Unitari"]

        iva = (fila["IVA"]/100)

        total_amb_iva  =  subtotal+iva

        if gran1 < total_amb_iva:
            gran1 = total_amb_iva 
            

        if gran2 < total_amb_iva and gran1!=total_amb_iva:
            gran2 = total_amb_iva 
            

        if gran3 < total_amb_iva and gran1!=total_amb_iva and gran2!=total_amb_iva:
            gran3 = total_amb_iva 

        

    resultat = [gran1,gran2,gran3]



    print("TOP 3 productes que han facturat més")
    print("Top 1:", resultat[0])
    print("Top 2:", resultat[1])
    print("Top 3:", resultat[2])

    

#Per últim crearem una funció anomenada menu que s'executara la primera.
def menu():
    
    print("-"*70)
    print("1. Calcular facturació del mes.")
    print("2. Calcular estoc disponible per a cada producte.")
    print("3. Resum dels 3 productes que més han facturat.")
    print("4. Sortir.")
    print("-"*70)

#Dins de la funció li demanarem amb una condició la opció que vol fer.
    opcio = int(input("Què vols fer? "))
    match opcio:
        case 1:
            calculFactMes()
        case 2:
            calcul_stock()
        case 3:
            productes_mes_facturats()
        case __: 
            print("Si us plau, posa un numero del 1 al 3. Graciés")

menu()