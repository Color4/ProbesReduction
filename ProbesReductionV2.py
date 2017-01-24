# -*- coding: cp1252 -*-

# Crée une liste vide "ProbeList"
ProbeList = []

# Ouvre le fichier entrée en mode "read"
with open(r"C:\Users\fernandez\Desktop\Tiling_tdt", "r") as EntryFile:

    # Boucle de lecture du fichier entrée, ligne après ligne    
    for Line in EntryFile:
        # Ajoute à la liste "sondes_init" la ligne lue, sous forme de liste (split)
        ProbeList.append(Line.split())
    
# Enregistre et retire l'entête
ProbeListFirst = ProbeList[0]
ProbeList.remove(ProbeList[0])
print ProbeListFirst

# Définie les variables de parcours de la liste "ProbeList"
TargetID = 0
BPStart = 1
Sequence = 2
ProbeLength = 3
EndDistance = 4

# Calcul et affiche le nombre de sondes initiales
print "ProbeList :", len(ProbeList), "sur 969251 attendues"

# Calcul et affiche le nombre de régions couvertes
TargetTag = ProbeList[0][TargetID]
TargetCount = 1
ProbeListEnum = range(len(ProbeList))
for Line in ProbeListEnum:
    if TargetTag != ProbeList[Line][TargetID]:
        TargetTag = ProbeList[Line][TargetID]
        TargetCount += 1
print "Nombre de régions couvertes :", TargetCount

# Parcours la liste "ProbeList" et vérifie les gap
ProbeListEnum = range(len(ProbeList))
r=0
for Probe in ProbeListEnum:
    DistCheck = int(ProbeList[Probe][1]) - int(ProbeList[Probe][1])
    if DistCheck > 60:
        #print "Error, gap detected in Target :", ProbeList[Probe][0], "between probe", ProbeList[Probe][1], "and probe",  ProbeList[Probe+1][1]
        r+=1
print r

# Crée une liste vide "TargetList"
TargetList =[]
TargetListEnum = range(TargetCount)
for Target in TargetListEnum:
    TargetList.append([])

# Remet à 0 les compteurs
TargetTag = ProbeList[0][TargetID]
TargetEnum = 0
# Boucle de lecture de la liste "ProbeList", ligne après ligne
for Line in ProbeListEnum:
    # Ajoute à la liste "TagetList.[TargetTag]" la ligne corespondante
    if TargetTag == ProbeList[Line][TargetID]:
        TargetList[TargetEnum].append(ProbeList[Line])
    else:
        TargetEnum += 1
        TargetList[TargetEnum].append(ProbeList[Line])
        TargetTag = ProbeList[Line][TargetID]

# Crée une liste vide "TargetProbeSelect"
TargetProbeSelect = []
for Target in TargetListEnum:
    TargetProbeSelect.append([])

# Parcours la liste "TargetList" et place les sondes remplissant les conditions dans la liste "TargetProbeSelect"
TargetProbeSelectEnum = range(len(TargetProbeSelect))
for Target in TargetProbeSelectEnum:
    ProbeListEnum = range(len(TargetList[Target]))
    TargetProbeSelect[Target].append(TargetList[Target][0])
    LastProbeSelect = 0
    for Probe in ProbeListEnum:
        distance = int(TargetList[Target][Probe][1]) - int(TargetList[Target][LastProbeSelect][1])
        if distance >= 60:
            TargetProbeSelect[Target].append(TargetList[Target][Probe-1])
        if distance >= 12:
            TargetProbeSelect[Target].append(TargetList[Target][Probe])
            LastProbeSelect = Probe
        
            
    if TargetList[Target][-1] not in TargetProbeSelect[Target]:
            TargetProbeSelect[Target].append(TargetList[Target][-1])





# Compte le nombre de sonde dans la liste "TargetList"
i = 0
for Target in TargetListEnum:
    i += len(TargetList[Target])

# Compte le nombre de sonde dans la liste "TargetProbeSelect"
j = 0
for Target in TargetProbeSelectEnum:
    j += len(TargetProbeSelect[Target])

print "TargetList :", i, " TargetProbeSelect :", j, "sur 969251 attendues"
if j > 969251:
    print j-969251, "sondes en trop !"
if j < 969251:
    print "Il manque", 969251-j, "sondes !"
if j == 969251:
    print "C'est bon, tu as tes", j, "sondes, ne touche plus à rien !"




# Parcours la liste "TargetProbeSelect" et vérifie les gap
TargetProbeSelectEnum = range(len(TargetProbeSelect))
p=0
for Target in TargetProbeSelectEnum:
    ProbeListEnum = range(len(TargetList[Target])-1)
    for Probe in ProbeListEnum:
        DistCheck = int(TargetList[Target][Probe+1][1]) - int(TargetList[Target][Probe][1])
        if DistCheck > 60:
            #print "Error, gap detected in Target :", TargetList[Target][0][0], "between probe", TargetList[Target][Probe][1], "and probe",  TargetList[Target][Probe+1][1]
            p+=1
print p



# Parcours la liste "TargetProbeSelect" et retire quelques sondes de la liste
TargetProbeSelectEnum = range(len(TargetProbeSelect))
FractionEnum = range(24)
for Target in TargetProbeSelectEnum:
    NbProbeTarget = len(TargetProbeSelect[Target])
    FreqFractionRemove = NbProbeTarget/24
    FractionRemove = FreqFractionRemove
    for Fraction in FractionEnum:
        #print NbProbeTarget, FreqFractionRemove, Fraction, FractionRemove
        TargetProbeSelect[Target].remove(TargetProbeSelect[Target][FractionRemove])
        FractionRemove += FreqFractionRemove-(FreqFractionRemove/24)-1





# Compte le nombre de sonde dans la liste "TargetList"
i = 0
for Target in TargetListEnum:
    i += len(TargetList[Target])

# Compte le nombre de sonde dans la liste "TargetProbeSelect"
j = 0
TargetProbeSelectEnum = range(len(TargetProbeSelect))
for Target in TargetProbeSelectEnum:
    j += len(TargetProbeSelect[Target])
    
print "TargetList :", i, " TargetProbeSelect :", j, "sur 969251 attendues"
if j > 969251:
    print j-969251, "sondes en trop !"
if j < 969251:
    print "Il manque", 969251-j, "sondes !"
if j == 969251:
    print "C'est bon, tu as tes", j, "sondes, ne touche plus à rien !"


# Parcours la liste "TargetProbeSelect" et vérifie les gap
TargetProbeSelectEnum = range(len(TargetProbeSelect))
t=0
for Target in TargetProbeSelectEnum:
    ProbeListEnum = range(len(TargetList[Target])-1)
    for Probe in ProbeListEnum:
        DistCheck = int(TargetList[Target][Probe+1][1]) - int(TargetList[Target][Probe][1])
        if DistCheck > 60:
            #print "Error, gap detected in Target :", TargetList[Target][0][0], "between probe", TargetList[Target][Probe][1], "and probe",  TargetList[Target][Probe+1][1]
            t+=1
print p        
