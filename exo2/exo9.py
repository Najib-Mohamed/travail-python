caratere = input("Entrez un nombre : ")
nobreValide = True
for i in range(len(caratere)):
    codeAscii = ord(caratere[i])
    if codeAscii < 48 or codeAscii > 57:
        print(f"Le code ASCII du caractère '{caratere}' est : {codeAscii}")
        print(f"Le caractère '{caratere}' n'est pas un chiffre.")
        nobreValide = False
        
if nobreValide:
    print(f"le nombre '{caratere}' est valide.")
else:
    print(f"le nombre '{caratere}' n'est pas valide.")