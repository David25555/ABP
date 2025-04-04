#Pas 1: Posarem el csv en el programa.

#Pas 2: Crearem una funció que sera llegir el text (izan)

import csv

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

#Pas 5: Calcular facturació del mes

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
 

#que pugui llegir la quantitat venuda, el preu unitari, el iva .
#I multipliquem les unitats venudes per el preu unitari i li sumarem el 21 per cent del IVA.


#Pas 6: Calcular stock disponible per a cada producte
def calcul_stock ():
    arxiu = "dades_botiga.csv"
    dades = carregar_dades(arxiu)
    print("ESTOC DISPONIBLE PER PRODUCTE")
    for fila in dades:
        print(fila["Producte"], ": ", fila["Estoc_Disponible"])
        
  


#Depend el producte que comprem, el restarem a la nostre de dades i si el usuari tornin a mirar la base de dades, estara actualitzada.

#Pas 7: - Resum dels 3 productes que més han facturat 
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

    


##Minecraft,Videojocs,50,34,21,71
        
  

#crearem un bucle que el que farà serà fer la fórmula de multiplicar les unitats venudes per el preu unitari i li sumarem el 21 per cent del IVA.

#i els 3 números més grans que li donen els imprimira en pantalla.

def menu():
    #Pas 3: Menú Principal 

    #El que farem sera crear un codi que llegiu el text i amb un return i un print ens mostri les dades.
    print("-"*70)
    print("1. Calcular facturació del mes.")
    print("2. Calcular estoc disponible per a cada producte.")
    print("3. Resum dels 3 productes que més han facturat.")
    print("4. Sortir.")
    print("-"*70)

    #Pas 4: Li pedirem al usuari que vol fer amb un mach case de les opcions que sera:
     
    #- Menú Principal 
    #- Calcular facturació del mes
    #- Calcular estoc disponible per a cada producte
    #- Resum dels 3 productes que més han facturat 
    opcio = int(input("Què vols fer? "))
    match opcio:
        case 1:
            calculFactMes()
        case 2:
            calcul_stock()
        case 3:
            productes_mes_facturats()
        case 4: 
            ()

menu()