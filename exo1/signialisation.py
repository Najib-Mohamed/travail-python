# ceci est une fonction qui permet de changer le feu de signialisation tout les 20 tour et ce 5 fois
# vartime est la variable qui prend en chatge le temps avant la changement de couleur de feu de signialisation
# var couleur prend en chatge la couelur
# varnbtour prend en charge le nombre de répétition pour ne pas avoir une boucle infi
varTime = 0
varcouleur = 3
varnbtour = 0
while varnbtour <= 5:
    if varTime == 20:
        if varcouleur == 3 :
            varTime = 0
            varcouleur = 2
            varnbtour = varnbtour +1
            print("feu rouge ne passez pas !")
        elif varcouleur == 2:
            print("feu oragne ralentissez et essayez de vous arretez")
            varTime = 0
            varcouleur = 1
            varnbtour = varnbtour +1
        else:
            print("feu vert vous pouvez conduire")
            varTime = 0
            varcouleur = 3
            varnbtour = varnbtour +1  
    varTime = varTime + 1
    print(varTime)
