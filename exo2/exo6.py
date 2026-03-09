caratere = input("Entrez une phrase : ")
nbchiffres = 0
for i in range(len(caratere)):
    codeAscii = ord(caratere[i])
    if codeAscii >= ord("0") and codeAscii <= ord("9"):
        print(f"Le code ASCII du caractère '{caratere}' est : {codeAscii}")
        print(f"Le caractère '{caratere}' est un chiffre.")
        nbchiffres += 1
    else:
        print(f"Le code ASCII du caractère '{caratere}' est : {codeAscii}")
        print(f"Le caractère '{caratere}' n'est pas un chiffre.")
print(f"Le nombre de chiffres dans la phrase est : {nbchiffres}")
