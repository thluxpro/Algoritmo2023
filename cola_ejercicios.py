from cola import Cola
from random import randint

cola = Cola()

# # #! carga
# for i in range(10):
#     value = chr(randint(65, 90))
#     print(value)
#     cola.arrive(value)

# #!  d, f, e, g, j, i, a
# print()
# cont = 0
# total = cola.size()
# while cont < total:
#     if cola.on_front() in ['A', 'E', 'I', 'O', 'U']:
#         cola.atention()
#     else:
#         cola.move_to_end()
#     cont += 1

# cont = 0
# while cont < cola.size():
#     value = cola.move_to_end()
#     print(value)
#     cont += 1
    


# Ejercicio primos
# def es_primo(numero):
#     cont=0
#     for i in range(2,numero):
#         if (numero % i == 0):
#             cont += 1
#             break
#         return cont == 0
    
            
# for i in range(10):
#     valor = randint(2, 20)
#     print('valor generado', valor)
#     cola.arrive(valor)

# cont = 0
# total = cola.size()
# while cont < total:
#     if es_primo(cola.on_front()):
#         cola.atention()
#     else:
#         cola.move_to_end()
#     cont += 1

# cont = 0
# while cont < cola.size():
#     print(cola.on_front())
#     cola.move_to_end()
#     cont += 1

#contar ocurrencias (Ej 6)

# for i in range(10):
#     valor = randint(0, 20)
#     print('valor generado', valor)
#     cola.arrive(valor)

# cont_ocurrencias = 0
# total = cola.size()
# cont= 0
# busca = input("ingrese un numero")
# busca = int(busca)
# while cont < total:
#     adelante= cola.on_front()
#     if (adelante == busca):
#         cola.atention()
#         cont_ocurrencias += 1
#     else:
#         cola.move_to_end()
#     cont += 1

# print(f'la cantidad de veces que se repite es{cont_ocurrencias}')    

#Ejercicio 7
cola_aux = Cola()
valores = [3, 5, 1, 4, 2]


for numero in valores:
    if cola_aux.size() == 0:
        cola_aux.arrive(numero)
    elif numero < cola_aux.on_front():
        cola_aux.arrive(numero)
        contador = 0
        while contador < cola_aux.size()-1:
            cola_aux.move_to_end()
            contador += 1
    else:
        pass


while cola_aux.size() > 0:
    print(cola_aux.atention())
