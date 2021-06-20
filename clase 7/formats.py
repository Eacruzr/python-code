num1 = 87
num2 = 42

mensaje = 'Los numeros son '+ str(num1)+', '+str(num2)
print(mensaje)
mensaje = 'Los numeros son {}, {}'.format(num1,num2)
print(mensaje)
mensaje = 'Los numeros son {1}, {0}, {2}'.format(num1,num2, 58)
print(mensaje)
mensaje = 'Los numeros son %d'%(num1)
print(mensaje)
mensaje = f'Los numeros son {num1}, {num2}'
print(mensaje)
