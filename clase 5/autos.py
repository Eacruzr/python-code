autos = {'autos':{
        1:{'marca':'Tesla',
           'modelos':{
               1:'Model S',
               2:'Model E',
               3:'Model X',
               4:'Model Y',
               }
           },
        2:{'marca':'Toyota',
           'modelos':{
               1:'Fortuner',
               2:'Prado',
               3:'Tundra',
               4:'Corola',
               }
           },
        3:{'marca':'Range Rover',
           'modelos':{
               1:'Evoque',
               2:'Defender',
               }
           },
        4:{'marca':'Mazda',
           'modelos':{
               1:'Mazda 3',
               2:'Mazda 2',
               3:'CX 30',
               }
           },
        5:{'marca':'Audi',
           'modelos':{
               1:'A7',
               2:'A5',
               3:'A3',
               }
           }
        }
        }

m1=len(autos['autos'][1]['modelos'])
m2=len(autos['autos'][2]['modelos'])
m3=len(autos['autos'][3]['modelos'])
m4=len(autos['autos'][4]['modelos'])
m5=len(autos['autos'][5]['modelos'])

def mas(m1,m2,m3,m4,m5):
    if m1 > m2 and m1 > m3 and m1 > m4:
        print('La marca con mayor numero de modelos es: '+m1)
    elif m2>m3 and m2>m4 and m2>m5:
        print(m2)
    elif m3>m4 and m3>m5:
        print(m3)
    elif m4>m5:
        print(m4)
    else:
        print(m5)