#Pas 1: Posarem el csv en el programa.


#Pas 2: Crearem una funció que sera llegir el text (izan)

import csv

notes =''
with open ('arxiu.csv', newline='') as f:
    data= csv.reader(f, delimiter= ',')
    notes= list(data)

#print(notes)
    
    def getdata(notes):
        for i in range(1, len(notes)):
            for x in range (len(notes[i])):
                print(notes[0][x] + ': ' + notes [i] [x] )
                print('')

    getdata(notes)

#Pas 3: Li pedirem al usuari que vol fer amb un mach case de les opcions que sera:

#- Menú Principal 
#- Calcular facturació del mes
#- Calcular estoc disponible per a cada producte
#- Resum dels 3 productes que més han facturat 


#Pas 4: Menú Principal 

#El que farem sera crear un codi que llegiu el text i amb un return i un print ens mostri les dades.



#Pas 5: Calcular facturació del mes

#que pugui llegir la quantitat venuda, el preu unitari, el iva .
#I multipliquem les unitats venudes per el preu unitari i li sumarem el 21 per cent del IVA.


#Pas 6: Calcular estoc disponible per a cada producte

#Depend el producte que comprem, el restarem a la nostre de dades i si el usuari tornin a mirar la base de dades, estara actualitzada.

#Pas 7: - Resum dels 3 productes que més han facturat 


#crearem un bucle que el que farà serà fer la fórmula de multiplicar les unitats venudes per el preu unitari i li sumarem el 21 per cent del IVA.

#i els 3 números més grans que li donen els imprimira en pantalla.

