def aprovados(dicionario):
    for i in dicionario:
        if False not in (x > 7 for x in dicionario[i]):
            print(i)
aprovados({'Darth Vader':(7.5,8.0,6.5),'Han Solo':(9.0,8.5,9.5),'Chewbacca':(3.5,1.0,6.5)})
