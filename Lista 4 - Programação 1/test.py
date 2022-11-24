lista = []
for i in range(31):
    lista.append("'c ("+str(i)+")'!F52+")
formula = ''
for i in lista:
    formula += i
print(formula)