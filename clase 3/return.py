def sumar(num1,num2,num3) -> float:
    total_local=num1 + num2 + num3
    return total_local

def promedio():
    num_1=float(input("Digite primer numero: "))
    num2=float(input("Digite segundo numero: "))
    num3=float(input("Digite tercer numero: "))
    total=sumar(num_1,num2,num3)
    return total/3

print(promedio())