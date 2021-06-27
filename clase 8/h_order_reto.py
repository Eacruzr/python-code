numeros = [3.1, 4.2, 4, 3.9, 3.2, 3.68, 4.01, 2.99]

def medio(colleccion):
    
    return colleccion[3]

def evaluar_lista(funcion, colleccion):
    print(funcion(colleccion))

evaluar_lista(medio, numeros)