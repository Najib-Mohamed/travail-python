caratere = input("Entrez un nobre : ")
somme = 0
for i in range(len(caratere)):
    codeAscii = ord(caratere[i])
    if codeAscii == ord("0") :
        somme = somme + 0
    elif codeAscii == ord("1") :
        somme = somme + 1
    elif codeAscii == ord("2") :
        somme = somme + 2
    elif codeAscii == ord("3") :
        somme = somme + 3
    elif codeAscii == ord("4") :
        somme = somme + 4
    elif codeAscii == ord("5") :
        somme = somme + 5
    elif codeAscii == ord("6") :
        somme = somme + 6
    elif codeAscii == ord("7") :
        somme = somme + 7
    elif codeAscii == ord("8") :
        somme = somme + 8
    elif codeAscii == ord("9") :
        somme = somme + 9
print(f"La somme des chiffres du nombre introduit est : {somme}")
