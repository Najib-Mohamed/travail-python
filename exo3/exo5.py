mot = input("Entrez un mot : ")
motInverse = ""
for i in mot:
    print(i)
    motInverse = i + motInverse

if motInverse == mot:
    print(f"Le mot '{mot}' est un palindrome. {motInverse}")
else:
    print(f"le mot a l'envert n'est pas un palindrome : {motInverse}")