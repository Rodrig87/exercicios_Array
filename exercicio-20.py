num = []
numimpar = []
numpar = []
numpos = []
numneg = []
zero = []

for x in range(10):
    n = int(input("Digite um número: "))
    num.append(n)

for n in num:
    if n % 2 == 0:
        numpar.append(n)
    else:
        numimpar.append(n)

    if n > 0:
        numpos.append(n)
    elif n < 0:
        numneg.append(n)
    else:
        zero.append(n)

print(f"Números ímpares: {numimpar}\nNúmeros pares: {numpar}\nNúmeros positivos: {numpos}\nNúmeros negativos: {numneg}\nZeros:{zero}")

