phrase = input("verillez introduire une phrase : ")
motActuelle = ""
motPlusLong = ""

for i in phrase:
    if i == " ":
        if len(motActuelle) > len(motPlusLong):
            motPlusLong = motActuelle
        motActuelle = ""
    else :
        motActuelle += i

if len(motActuelle) > len(motPlusLong):
    motPlusLong = motActuelle
    
print(motPlusLong)