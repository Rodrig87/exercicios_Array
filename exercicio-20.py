a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for c in range(10):
    a[c] = int(input("Digite um número: "))
for m in range(10):
    if a[m] %2 == 0:
        print(f"Esse número é par {a[m]}")
    else:
        print(f"Esse número é impar {a[m]}")
    if a[m] > 0:
        print(f"Esse número é positivo {a[m]}")
    elif a[m] < 0:
        print(f"Esse número é negativo {a[m]}")
    else:
        print(f"Esse número é zero {a[m]}")
