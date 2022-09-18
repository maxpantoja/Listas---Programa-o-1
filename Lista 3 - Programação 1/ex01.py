x, x1, x2, x3, x4 = 0, 0, 0, 0, 0
while x >= 0:
    x = float(input("Digite o número: "))
    if x in range(0, 26):
        x1 += 1
    if x in range(26, 51):
        x2 += 1
    if x in range(51, 76):
        x3 += 1
    if x in range(76, 100):
        x4 += 1
print(f'''[0-25]: {x1}
[26-50]: {x2}
[51-75]: {x3}
[76-100]: {x4}''')
