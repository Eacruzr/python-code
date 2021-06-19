def calcular_tiempo_recorrido(numero_abordados, numero_desc)->float:
    tiempo_recorrido_parcial= 90/30
    tiempo_mas=(numero_abordados*(1/30))+(numero_desc*(1/60))
    tiempo_total=tiempo_recorrido_parcial+tiempo_mas
    return tiempo_total

numero_abordados=float(input("Digite el numero de pasajeros abordados: "))
numero_desc=float(input("Digite el numero de pasajeros que descendieron: "))
print("El bus se demora "+str(calcular_tiempo_recorrido(numero_abordados,numero_desc)*60)+" minutos")