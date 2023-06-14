from lista import Lista
from cola import Cola

class Avengers:
    def __init__(self,superheroe,nombreheroe,grupo,aparicion):
        self.superheroe = superheroe
        self.nombreheroe = nombreheroe
        self.grupo = grupo
        self.aparicion = aparicion 
    def __str__(self):
        return f'{self.superheroe} {self.nombreheroe} {self.grupo} {self.aparicion}'
    
personajes = [
        {'heroe':'mr. fantastico','name':'reed richards','group':'cuatro fantasticos','year':1961},
        {'heroe':'human torch','name':'jhonny storm','group':'cuatro fantasticos','year':1961},
        {'heroe':'star lord','name':'peter quill','group':'guardianes de la galaxia','year':1975},
        {'heroe':'mujer invisible','name':'susan storm','group':'cuatro fantasticos','year':1961},
        {'heroe':'vlank widow','name':'natasha romanoff','group':'vengadores','year':1964},
        {'heroe':'groot','name':'groot','group':'guardianes de la galaxia','year':1962},
        {'heroe':'rocket raccoon','name':'rocket raccoon','group':'guardianes de la galaxia','year':1960},
        {'heroe':'hulk','name':'bruce banner','group':'','year':1962},
        {'heroe':'iron man','name':'tony stark','group':'vengadores','year':1963},
        {'heroe':'capitana marvel','name':'carol danvers','group':'vengadores','year':1986},
        {'heroe':'spider man','name':'peter parker','group':'vengadores','year':1980}, 
        {'heroe':'ant man','name':'henry pym','group':'vengadores','year':1990},
        {'heroe':'capitan america','name':'steve roger','group':'vengadores','year':1903},
        {'heroe':'black panter','name':'TChalla','group':'vengadores','year':2000},
        {'heroe':'falcon','name':'Sam Wilson','group':'vengadores','year':1900},
        {'heroe':'doctor strange','name':'Stephen Strange','group':'vengadores','year':1999},
        {'heroe':'hawkeye','name':'clint barton','group':'vengadores','year':1963},
        {'heroe':'thor','name':'thor odinson','group':'vengadores','year':2005},
        {'heroe':'vision','name':'vision','group':'vengadores','year':2010},
        {'heroe':'war machine','name':'James Rhodes','group':'vengadores','year':2010},
        ]

lista=Lista()
for personaje in personajes:
    lista.insert(Avengers(personaje['heroe'].title(),
                             personaje['name'].title(),
                             personaje['group'].title(),
                             personaje['year'],
                             ),'superheroe')
print('')
# punto a 
data = lista.get_element_by_index(lista.search('Capitana Marvel','superheroe'))
if data is not None:
    print(f'{data.superheroe} se encuentra en la lista')
else:
    print(f'{data.superheroe} no esta en la lista')

cola=Cola()
#punto b
for i in range(lista.size()):
    data=lista.get_element_by_index(i)
    if data.grupo == 'Guardianes De La Galaxia':
        cola.arrive(data)
print(f"la cantidad de personajes de guardianes de la galaxia son {cola.size()}")
print("") 

#punto C

print('barrido decendente de los guardianes de la glaaxia')
for i in range(lista.size()-1,-1,-1):
    data= lista.get_element_by_index(i)
    if data.grupo =='Guardianes De La Galaxia':
        print(data)
print("")       
print('barrido decendente de los guardianes de los cuatro fantasticos')
for i in range(lista.size()-1,-1,-1):
    data= lista.get_element_by_index(i)
    if data.grupo =='Cuatro Fantasticos':
        print(data)
        
#punto d

for i in range(lista.size()):
    data=lista.get_element_by_index(i)
    if data.aparicion > 1960:
        print(f"los personajes cuyo año de aparicion mayor a 1960 son {data.superheroe}")

data=lista.get_element_by_index(lista.search('Vlank Widow','superheroe'))
if data is not None:
    data.superheroe = 'Black Widow'
    print("se modifico el nombre")
else:
    print("no se encuentra en la lista")
lista.order_by('superheroe')
# lista.barrido()
#punto g
for i in range(lista.size()):
    data=lista.get_element_by_index(i)
    if data.superheroe[0] in ['C','P','S']:
        print(f"los personajes que empiezan con C, P o S son {data.superheroe}")