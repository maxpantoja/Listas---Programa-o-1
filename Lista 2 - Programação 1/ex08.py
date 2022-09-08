from datetime import datetime
data = str(input("Informe a data (00/00/0000): "))
try:
    res = bool(datetime.strptime(data, "%d/%m/%Y"))
except ValueError:
    res = False
if res:
    print("Sua data é válida!")
else:
    print("Sua data não é válida!")
