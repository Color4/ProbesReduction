# -*- coding: cp1252 -*-

with open(r"C:\Users\Alexandre\Desktop\Tiling_tdt", "r") as fichier_entree:
    for ligne in fichier_entree:
        regions.append(ligne.split())
        
regions.remove(regions[0])

print "nombre de regions initiales : ", len(regions)

indice = 0
                                           
while indice < len(regions):

    distance = int(regions[indice+1][1]) - int(regions[indice][1])
    if distance <= 6 and distance > 0:
        regions.remove(regions[indice+1])                         
    else:
        indice += 1
                                   
print "nombre de regions finales : ", len(regions)
