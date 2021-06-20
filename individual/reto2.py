sesion = True
opciones = ['1. Cambiar contraseña','2. Ingresar coordenadas actuales','3. Ubicar zona wifi mas cercana','4. Guardar archivo con ubicación cercana','5. Utilizar registros de zona wifi desde archivo','6. Elegir opcion de menu favorita','7. Cerrar sesión']

while sesion:
    for opt in opciones:
        print(opt)
    option = input('Elija una opción: ')
    
    if option =='6':
        resul = input('Cuanto es 5 + 7: ')
        if resul == '12':
            opcion = input('Digite la opcion que desea poner como favorita: ')
            if int(option)>=1 and int(option)<=5:
                opciones.remove(opcion)
                opciones.insert(0,opcion)
                print(opciones)
        else:
            sesion = False
    elif option == '7':
        print('Nos fuimos')
        sesion = False
    