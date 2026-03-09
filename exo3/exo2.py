mot = input("Entrez un mot : ")
lettre = input("Entrez une lettre pour voir combien de fois elle apparaît dans le mot : ")

compteur = 0

for i in mot:
    if i == lettre:
        compteur += 1
print(f"La lettre '{lettre}' apparaît {compteur} fois dans le mot '{mot}'.")

