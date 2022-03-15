# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 17:58:25 2022

@author: 47944
"""

#a og b
tid=float(input("Hvor mange sekunder har objektet falt?  "))
while tid < 0:
    print("Negativ tid mister?")
    tid=float(input("Hvor mange sekunder har objektet falt?  "))
resultat_fart=9.81*tid
resultat_strekning=0.5*resultat_fart*tid
print(f"{resultat_fart} meter/sekund og strekning {resultat_strekning} meter")


#c
pris=float(input("Prisen på den da mister?  "))
resultat_pris=0
while pris > 0:
    resultat_pris += pris
    print(resultat_pris)
    pris=float(input("Prisen på den da mister?  "))
    
    
print(resultat_pris)
      
#d
tid_start=int(input("Hvor vil du starte å måle tid?  "))
tid_slutt=int(input("Hvor vil du slutte å måle tid?  "))
intervaller=int(input("Hvor mange intervaller ønsker du   "))
while tid_start < 0:
    print("Negativ tid mister?")
    tid_start=int(input("Hvor vil du starte å måle tid?  "))
while tid_slutt < tid_start:
    print("Slutttiden kommer etter starttiden kompis")
    tid_slutt=int(input("Hvor vil du slutte å måle tid?  "))
while intervaller <= 0:
    print("Negative intervaller?")
    intervaller=int(input("Hvor mange intervaller ønsker du   "))
antall_målinger=int((tid_slutt-tid_start)/intervaller)

for tid in range(tid_start,tid_slutt,antall_målinger):
    resultat_fart2=9.81*tid
    resultat_strekning2=0.5*resultat_fart2*tid    
    print(f"{resultat_fart2} meter/sekund og strekning {resultat_strekning2} meter ved {tid}")