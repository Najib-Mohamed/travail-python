phrase = input("Entrez une phrase ")
estDM = False
cnt = 0

for i in phrase:
    if i == " ":
        estDM = False
    else:
        if not estDM:
            estDM = True
            cnt+=1
print(cnt)