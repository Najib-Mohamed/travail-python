nombre = input("Entrez un nombre : ")
nbstring = ""
nbstring1 = ""
nombreint2 = int(nombre)
for i in range(len(nombre)):
    nbstring = nbstring + str(nombreint2 % 10)
    print(nombreint2 % 10)
    nombreint2 = nombreint2 // 10
print(f"Le nombre inversé est : {nbstring}")

nombreint = int(nombre)
for i in range(len(nombre)):
    print(nombreint // 10**(len(nombre)-(i+1)))
    nbstring1 = nbstring1 + str(nombreint // 10**(len(nombre)-(i+1)))
    nombreint = nombreint % 10**(len(nombre)-(i+1))
print(f"Le nombre est : {nbstring1}")