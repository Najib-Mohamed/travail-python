mot = input("Entrez un mot : ")

compteur = 0

for i in mot:
    if i in "aeiouy":
        compteur += 1

if compteur > 0:
    print(f"Le mot '{mot}' contient {compteur} voyelle(s).")
else:
    print(f"Le mot '{mot}' ne contient aucune voyelle.")