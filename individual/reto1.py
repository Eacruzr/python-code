print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
nombre_usuario='51593' #El usuario definido
contraseña='39515' #La contraseña definida
dato_usuario=input('Ingrese el nombre de usuario: ') #Se solicita el usuario a la persona

if dato_usuario==nombre_usuario: #Se compara el usuario ingresado con el del sistema para hacer la verificacion
    dato_contraseña=input('Ingrese la contraseña: ') #Se solicita la contraseña al usuario

    if dato_contraseña==contraseña: #Se compara la contraseña ingresada con la registrada en el sistema
        print("Solucione el captcha de seguridad")
        segundo_dato=5*3-5-1
        valor_captcha=593+segundo_dato #El valor del captcha
        captcha=int(input("Solucione 593+9 = ")) #Se solicita al usuario que ingrese la solucion del captcha
        #5*3-5-1=9/(3%5)+5+1=9/(5+5)-(1%3)=9/(5-3)*5-1=9
        if valor_captcha==captcha: #Se compara el dato ingresado por el usuario y el que esta en el sistema
            print("Sesión iniciada") #Se verifica que el proceso fue correcto

        else:
            print("Error") #Hubo un fallo en algun momento del proceso
    else:
        print("Error")
else:
    print("Error")