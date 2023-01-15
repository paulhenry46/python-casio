def complementaire(x) :

    l = list(x)
    for i in range(len(x)):

        if(l[i]=='G'):
            l[i]='C'

        elif(l[i]=='C'):
            l[i]='G'

        elif (l[i] == 'T'):
            l[i] = 'A'

        elif (l[i] == 'A'):
            l[i] = 'T'

        else:
            print('ADN invalide')

    print("Brin ARN complémentaire : ",end="")
    for char in l:
        print(char,end="")

x = (input("Brin ADN"))
print("Brin ADN : " + x)
complementaire(x) 
