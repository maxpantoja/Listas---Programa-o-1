numero = str(int(input("Insira um número inteiro menor que 1000: ")) + 1000)
un = int(numero[3])
dez = int(numero[2])
cen = int(numero[1])
lista = [cen, dez, un]
listax = []
for i in lista:
    if i > 1:
        listax.append("s")
    else:
        listax.append("")
if cen != "0":
    print(f"{int(numero) - 1000} = {cen} centena{listax[0]}, {dez} dezena{listax[1]} e {un} unidade{listax[2]}.")
if cen == "0" and dez != "0":
    print(f"{int(numero)-1000} = {dez} dezena{listax[1]} e {un} unidade{listax[2]}.")
elif dez == "0":
    print(f"{int(numero)-1000} = {un} unidade{listax[2]}.")
