caratere = input("Entrez une lettre : ")
codeAscii = ord(caratere)

if codeAscii >= ord("A") and codeAscii <= ord("Z"):
    print(f"Le code ASCII du caractère '{caratere}' est : {codeAscii}")
    print(f"Le caractère '{caratere}' est une lettre majuscule.")
elif codeAscii >= ord("a") and codeAscii <= ord("z"):
    print(f"Le code ASCII du caractère '{caratere}' est : {codeAscii}")
    print(f"Le caractère '{caratere}' n'est pas une lettre majuscule.")
else:
    print(f"Le code ASCII du caractère '{caratere}' est : {codeAscii}")
    print(f"Le caractère '{caratere}' n'est pas une lettre.")