phrase = input("Entrez une phrase : ")


while phrase[0]==" " or phrase[-1]==" ":
    for i in range(len(phrase)):
        if phrase[0] == " " and phrase[len(phrase)-1] == " ":
            phrase = phrase[1:]+phrase[:1]
        elif phrase[0] == " " and phrase[len(phrase)-1] != " ":
            phrase = phrase[1:]+phrase[:0]
        elif phrase[0] != " " and phrase[len(phrase)-1] == " ":
            phrase = phrase[0:-1]
    
    print(f"début{phrase}fin")
