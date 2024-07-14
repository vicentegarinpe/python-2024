#ejrrcicio 
AlturasZonaCentral=(8848, 8611, 8586, 8200, 8460, 8200)
AlturasZonaSur= (8848, 5567, 8125, 4560, 8051, 4560)
AlturasZonaAustral= (2200, 2500, 1000, 2200, 3623, 990)

#A
a_set={AlturasZonaAustral}
a_set2={AlturasZonaSur}
a_set3={AlturasZonaCentral}

intersection=a_set.intersection(a_set2)
intersection2=a_set3.intersection(intersection)

(intersection)
(intersection2)

#tranformar a set para poder hacer la c

aset={AlturasZonaCentral}
aset2={AlturasZonaSur}
aset3={AlturasZonaAustral}

union1=aset.union(aset2)
union2=aset2.union(union1)

#unir tuplas

tuplaunida=(tuple(union1+union2))


lista=[tuplaunida]

