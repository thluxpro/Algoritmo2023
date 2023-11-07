from arbol_binario import BinaryTree

lista_pokemones = [
    {'name': 'pikachu', 'number': 1, 'type':['electrico']},
    {'name': 'charmander', 'number': 5, 'type':['fuego']},
    {'name': 'bulbasor', 'number': 3, 'type':['planta']},
    {'name': 'sceptile', 'number': 25, 'type':['planta']},
    {'name': 'charizard', 'number': 7, 'type':['electrico']},
    {'name': 'blastoise', 'number': 12, 'type':['agua']},
    {'name': 'jolteon', 'number': 50, 'type':['electrico']},
    {'name': 'lycanroc', 'number': 20, 'type':['roca']},
    {'name': 'tyrantrum', 'number': 45, 'type':['roca']},

]
# punto a 
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipos = BinaryTree()

for data in lista_pokemones:
    names = data['name']
    numbers = data['number']
    types = data['type']

    arbol_nombre.insert_node(names, data)
    arbol_numero.insert_node(numbers, data)
    for type in types:
        arbol_tipos.insert_node(type, data)

num = 25
value = arbol_numero.search(num)
if value:
    print(value.other_values) 
else:
    print(f'no hay pokemon con el numero {num}')
# punto b
print('\nbusqueda por coincidencia')
nombre_buscado = arbol_nombre.search_by_coincidence('bul')
if nombre_buscado:
    print('pokémons encontrados por nombre')
    for pokemon in nombre_buscado:
        print('nombre', pokemon.value)
        print('datos', pokemon.other_values)
# punto d
print('\nlistado por numero ascendente')
arbol_numero.postorden()
print('\nlistado ascendente nombre ')
arbol_nombre.postorden()
print('\nlistado por nivel nombre')
arbol_nombre.by_level()


# punto e
print('\ndatos de jolteon')
node = arbol_nombre.search('jolteon')
if node:
    print(node.other_values)
else:
    print('no se encuentra jolteon')

print('\ndatos de lycanroc')
node = arbol_nombre.search('lycanroc')
if node:
    print(node.other_values)
else:
    print('no se encuentra lycanroc')

print('\ndatos de tyrantrum')
node = arbol_nombre.search('tyrantrum')
if node:
    print(node.other_values)
else:
    print('no se encuentra tyrantrum')

# punto f
print('\ncantidad de pokemons de tipo electrico')
cantidad = arbol_tipos.contar_tiposelectrico()
print(cantidad)   

print('\ncantidad de pokemons de tipo acero')
cantidad = arbol_tipos.contar_tiposacero()
print(cantidad) 

# punto c 
tipo = 'electrico'
print(f'\npokemons de tipo {tipo}')
arbol_tipos.inorden_tipos_pokemon(tipo)

# values = arbol_nombre.search_by_coincidence()
        
# arbol_nombre.inorden() 
# arbol_numero.inorden()
# arbol_tipos.inorden()       