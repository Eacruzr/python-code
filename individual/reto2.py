from os import system
sesion = True

menu = ['. Cambiar contraseña', '. Ingresar coordenadas actuales', '. Ubicar zona wifi más cercana', '. Guardar archivo con ubicación cercana', '. Actualizar registros de zonas wifi desde archivo', '. Elegir opción de menú favorita', '. Cerrar sesión']
#                 0                             1                                  2                                    3                                                4                                               5                          6       
while sesion == True:
    
    i = 0
    while i < len(menu):
        print(str(i+1)+menu[i])
        i+=1
        
    opcion = int(input('Elija una opción: '))
    
    if opcion>=1 and opcion<=7:
        print('Usted ha elegido la opcion',opcion)
    
        if opcion == 6:
            opc_fa = int(input('Seleccion opcion favorita '))
            if opc_fa>=1 and opc_fa<=5:
                adv_1 = input('Para confirmar por favor responda: El pato hace CUA y duerme en un TROnco, la respuesta es: ')
                if adv_1 == '4':
                    adv_2 = input('Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es: ')
                    if adv_2 == '3':
                        print('Su opcion favorita es: ', opc_fa)
                        #agg = menu[opc_fa-1]
                        #menu.remove()
                        #menu.append(0,agg)
                    else:
                        system("cls")
                else:
                    system("cls")
            else:
                print('Error')
                sesion = False
        if opcion == 7:
            print('Hasta pronto')
            sesion = False
    else:
        system("cls")
        sesion = False
    