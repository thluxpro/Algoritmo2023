from cola import Cola
from pila import Pila
#ejercicio 10

notificaciones =[
    {'app':'instagram','hora':'15:57','mensaje':'estas en casa?'},
    {'app':'twitter','hora':'09:30','mensaje':'te comparto este curso de python'},
    {'app':'instagram','hora':'11:43','mensaje':'te envio un meme'},
    {'app':'facebook','hora':'12:00','mensaje':'fulanito te hablo'},
    {'app':'facebook','hora':'15:00','mensaje':'menganito te hablo'},

                 ]
cola=Cola()
pila=Pila()
for  notifis in notificaciones:
    cola.arrive(notifis)
#punto a
cont=0
cont2=0
cont3=0
while cola.size() >= cont:
    dato=cola.atention()
    #print(dato)
    if dato['app'] != 'facebook':
        cola.arrive(dato)
    cont += 1
#punto b
while cola.size()  >= cont2:
    dato=cola.move_to_end()
    if dato['app'] == 'twitter' and  'python' in dato['mensaje']:
        print(dato['app'], dato['mensaje'])
    cont2 += 1
#punto c, comentar punto a para que tome toda la cola    
while cola.size() >= cont3:
    dato = cola.move_to_end()
    if dato['hora'] >= '11:43' and dato['hora'] <= '15:57':
        pila.push(dato)
    cont3 += 1
print ('la cantidad de elementos que quedaron en la pila son', pila.size())
print("")
while cola.size() > 0:
    print(cola.atention())


#ejercicio 22
class Heroes():
    def __init__(self, name, heroe, sex):
        self.name = name
        self.heroe = heroe
        self.sex = sex
    
    def __str__(self):
        return f'{self.name}  {self.heroe}  {self.sex}' 
    
superheroes=[
    {'nombre':'Tony Stark','hero':'Iron Man','sexo': 'M'},
    {'nombre':'Steve Rogers','hero':'Capitan America','sexo': 'M'},
    {'nombre':'Natasha Romanoff','hero':'Black Widow','sexo': 'F'},
    {'nombre':'Carol Danvers','hero':'Capitana Marvel','sexo': 'F'},
    {'nombre':'Scott Lang','hero':'Ant-Man','sexo': 'M'},
    {'nombre':'Peter Parker','hero':'Spider-Man','sexo': 'M'},
    ]
colaH=Cola()
for superheroe in superheroes:
        colaH.arrive(Heroes(superheroe['nombre'].title(),
                       superheroe['hero'].title(),
                       superheroe['sexo'].title(),
                       ))
cont = 0
encontrado= False
while colaH.size() > 0:
    dato=colaH.atention()
    #punto a
    if dato.heroe == 'Capitana Marvel'.title():
        print(f'el nombre de {dato.heroe} es {dato.name}')    
    #punto b
    if dato.sex == 'f'.title():
        print(f'el nombre de {dato.heroe} es {dato.name}')
    #punto C
    if dato.sex == 'm'.title():
        print(f'el nombre de {dato.heroe} es {dato.name}')
    if dato.heroe == 'Scott Lang'.title():
        print(f'el nombre de {dato.heroe} es {dato.name}')
    if dato.heroe[0] == 'S':
        print(f'los que comienzan con s son {dato.heroe}')
    #punto D
    if dato.name == 'Carol Danvers'.title():
        encontrado=True
        nombreH=dato.heroe
    cont += 1
#punto D 
if encontrado == True:
    print(f'Carol Danvers se encuentra en la cola y su nombre de heroe es {nombreH}')
else:
    print('no se encuentra en la cola')
       