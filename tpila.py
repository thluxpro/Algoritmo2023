from pila import Pila
#Ejercicio 19
###
class Pelicula():

    def __init__(self, title, year, produced):
        self.__title = title
        self.__year = year
        self.__produced = produced
    
    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year
    
    def get_produced(self):
        return self.__produced

    def __str__(self):
        return f'{self.__title} - {self.__year} - {self.__produced}'


pelis = [
    #* class
    Pelicula('El Sorprendente Hombre Araña 2', 2014, 'Marvel studios'),
    Pelicula('Annabelle', 2014, 'Warner Bros'),
    Pelicula('Spider-Man: un nuevo universo', 2018, 'Sony Pictures'),
    Pelicula('Los increíbles 2', 2018, 'Diney'),
    Pelicula('Capitán América: Civil War', 2016, 'Marvel studios'),
    Pelicula('Deadpool', 2018, 'Marvel studios'),
]


pila_1 = Pila()
for peli in pelis:
    pila_1.push(peli)
cont=0
while pila_1.size() > 0:
    dato = pila_1.pop()
    # punto a
    if dato.get_year() == 2014:
        print(dato.get_title(), 'se estreno en el 2014')
    #punto b
    if dato.get_year() == 2016:
        cont +=1
    #punto c
    if dato.get_produced()== 'Marvel studios':
        print(dato.get_title(), 'es de marvel')
print('la cantidad de peliculas estrenadas en 2016 es ',cont)

#Ejercicio 24
class PeliculaMarvel():

    def __init__(self, name, films):
        self.__name = name
        self.__films = films

    
    def get_name(self):
        return self.__name

    def get_films(self):
        return self.__films


    def __str__(self):
        return f'{self.__name} - {self.__films}'

pila_1= Pila()
    
personajes = [
        PeliculaMarvel('doctor strange', 4),
        PeliculaMarvel('groot', 3),
        PeliculaMarvel('spider-man', 5),
        PeliculaMarvel('black widow', 2),
        PeliculaMarvel('capitán América', 6),
        PeliculaMarvel('rocket raccon', 3),
        PeliculaMarvel('iron man', 7),
        ]


for personaje in personajes:
    pila_1.push(personaje)

cont1=0
cont2=0
while pila_1.size() > 0:
    dato= pila_1.pop()
    #punto A
    if dato.get_name() == 'groot':
        print('groot esta en la posicio', cont1+1)
    cont1 += 1
    #punto A
    if dato.get_name() == 'rocket raccon':
        print('rocket raccon esta en la posicion', cont2+1)
    cont2 += 1
    #punto B
    if dato.get_films() >  5:
        print(f'{dato.get_name()} aparece en {dato.get_films()} peliculas')
    if dato.get_name() == 'black widow':
    #punto C
        print(f'{dato.get_name()} aparece en {dato.get_films()} peliculas')
    #punto D
    if dato.get_name()[0] == 'c' or dato.get_name()[0] == 'd' or dato.get_name()[0] == 'g':
        print(f'los personajes que empiezan asi son {dato.get_name()}')
        