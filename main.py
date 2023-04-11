grau = int(input("Digite um valor pro grau da equação: "))

valor = grau

if grau < 1 or grau > 2:
    print("Grau inválido")

if valor == 1:
    print("A equação é do primeiro grau.")
    a = float(input("Digite o valor de a: "))
    if a == 0:
        print("Valor de a inválido")
    else:
        b = float(input("Digite o valor de b: "))
        calculo1 = -b / a
        print(f"{calculo1:.2f}")

if valor == 2:
    print("A equação é do segundo grau.")
    a = float(input("Digite o valor de a: "))
    if a == 0:
        print("Valor de a inválido")
    elif a != 0:
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        calculo2 = b**2 - 4 * a * c
        raiz1 = (-b + (calculo2 ** (1/2))) / 2 * a
        raiz2 = (-b - (calculo2 ** (1/2))) / 2 * a

        if calculo2 < 0:
            print("A equação não possui raízes reais")
    
        else:
            if calculo2 == 0:
                print(f"A equação possui apenas uma raíz real, {raiz1:.2f}")
            if calculo2 > 0:
                print(f"A equação possui duas raízes reais, {raiz1:.2f}, {raiz2:.2f}")
