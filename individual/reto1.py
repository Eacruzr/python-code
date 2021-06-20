print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
nombre_usuario='51743' #El usuario definido
contraseña='34715' #La contraseña definida
dato_usuario=input('Ingrese el nombre de usuario: ') #Se solicita el usuario a la persona

if dato_usuario==nombre_usuario: #Se compara el usuario ingresado con el del sistema para hacer la verificacion
    dato_contraseña=input('Ingrese la contraseña: ') #Se solicita la contraseña al usuario

    if dato_contraseña==contraseña: #Se compara la contraseña ingresada con la registrada en el sistema
        print("Solucione el captcha de seguridad")
        segundo_dato=2*4+8-12
        valor_captcha=743+segundo_dato #El valor del captcha
        captcha=int(input("Solucione 743+4 = ")) #Se solicita al usuario que ingrese la solucion del captcha
        if valor_captcha==captcha: #Se compara el dato ingresado por el usuario y el que esta en el sistema
            print("Sesión iniciada") #Se verifica que el proceso fue correcto
        else:
            print("Error") #Hubo un fallo en algun momento del proceso
    else:
        print("Error")
else:
    print("Error")