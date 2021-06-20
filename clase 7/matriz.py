lista = [5,4,6,8]

matriz = [lista, lista, lista]

# print(matriz[0])
# print(matriz[1])
# print(matriz[0][1])
# print(matriz[-1][-1])

matriz = [[5, 7, 6, 9], [3, 4, 2, 8], [7, 9, 6, 1]]
print(matriz)
i = 0
while i < len(matriz):
    j = 0
    while j < len(matriz[i]):
        if matriz[i][j] < 4:
            matriz[i][j] = input("Ingrese el nuevo valor que quiera colocar para esta posición: ")
        j+=1
    i+=1
print(matriz)   
