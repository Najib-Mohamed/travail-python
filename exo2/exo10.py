nb1 = input("Entrez un premier nombre : ")
nb2 = input("Entrez un deuxiemme nombre : ")

def convertChiffres(caratere):
    nombre = 0
    for i in range(len(caratere)):
        codeAscii = ord(caratere[i])
        if codeAscii == ord("0") :
            nombre = nombre * 10 +  0
        elif codeAscii == ord("1") :
            nombre = nombre * 10 +  1
        elif codeAscii == ord("2") :
            nombre = nombre * 10 +  2
        elif codeAscii == ord("3") :
            nombre = nombre * 10 +  3
        elif codeAscii == ord("4") :
            nombre = nombre * 10 +  4
        elif codeAscii == ord("5") :
            nombre = nombre * 10 +  5
        elif codeAscii == ord("6") :
            nombre = nombre * 10 +  6
        elif codeAscii == ord("7") :
            nombre = nombre * 10 +  7
        elif codeAscii == ord("8") :
            nombre = nombre * 10 +  8
        elif codeAscii == ord("9") :
            nombre = nombre * 10 +  9
    print(f"Le nombre introduit est : {nombre}")
    return nombre

somme = convertChiffres(nb1) + convertChiffres(nb2)
print(f"La somme des deux nombres est : {somme}")