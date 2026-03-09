caratere = input("Entrez un caractère : ")
codeAscii = ord(caratere)

if codeAscii >= ord("0") and codeAscii <= ord("9"):
    print(f"Le code ASCII du caractère '{caratere}' est : {codeAscii}")
    print(f"Le caractère '{caratere}' est un chiffre.")
else:
    print(f"Le code ASCII du caractère '{caratere}' est : {codeAscii}")
    print(f"Le caractère '{caratere}' n'est pas un chiffre.")