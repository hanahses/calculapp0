x = float(input(f"Insira o primeiro número: "))
y = float(input(f"Insira o segundo número: "))
op = input("Insira a operação: (+ - * /): ")

if op == "+":
    print(x+y)

elif op == "-":
    print(x-y)

elif op == "*":
    print(x*y)

elif op == "/":
    if y == 0:
        y = float(input(f"Divisão por 0, insira um denominador válido \n"))
        print(x/y)
    else: 
        print(x/y) 
else:
    print("Operador inválido, rode o programa novamente")
    
