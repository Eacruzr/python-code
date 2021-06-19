students = {'a': {'name':'Juan','notas':[3.1,4.2,4,3.9,3.2]}, 'j': {'name':'Jenny','notas':[4,3.7,4,4,4.2]},\
        'c': {'name':'Ana','notas':[4.1,4.7,4.1,4.9,4.2]}, 'y': {'name':'Pedro','notas':[4,3.7,4,4,4.2]},\
            'x': {'name':'Pablo','notas':[4,3.3,3.4,3.2,3.2]}, 'l': {'name':'Carlos','notas':[3.4,3.8,4.2,4,4.1]},\
                'v': {'name':'Maria','notas':[4.8,4.7,4.6,4.9,4.8]}, 'r': {'name':'Luisa','notas':[4.8,4.7,4.5,4.5,4.9]},\
                    'b': {'name':'Mario','notas':[2.4,3.2,3.1,3.4,4.2]}, 'g': {'name':'Fabio','notas':[2.4,3.2,3.1,3.4,4.2]}}

promediomayor=0
promediomenor=100
notamayor=0
notamenor=100
for key, value in students.items():
    # print(value['name'])
    promedio=sum(value['notas'])/len(value['notas'])
    for n in value['notas']:
        if n>notamayor:
            notamayor=n
            snmayor=value['name']
        if n<notamenor:
            notamenor=n
            snmenor=value['name']
    # print(promedio)
    if promedio>promediomayor:
        promediomayor=promedio
        smayor=value['name']
    if promedio<promediomenor:
        promediomenor=promedio
        smenor=value['name']
            
print('El/la estudiante con promedio mayor es '+ str(smayor)+ ' con promedio '+ str(promediomayor))    
print('El/la estudiante con promedio menor es '+ str(smenor)+ ' con promedio '+ str(promediomenor))
print('la nota mayor es ' + str(notamayor)+' de '+ str(snmayor))
print('la nota menor es ' + str(notamenor)+' de '+str(snmenor))
        
