from lista import Lista
from random import randint


lista_valores = Lista()


# #! carga
# for i in range(30):
#     lista_valores.insert(chr(randint(65, 90)))


# vocales = ['A', 'E', 'I', 'O', 'U']

# lista_valores.barrido()
# print()
# contador = 0
# while contador < lista_valores.size():
#     value = lista_valores.get_element_by_index(contador)
#     if value in vocales:
#         print(lista_valores.delete(value))
#     else:
#         contador += 1


# print()
# lista_valores.barrido()


for i in range(30):
    lista_valores.insert(chr(randint(65, 90)))
    

def es_primo(numero):
    cont=0
    for i in range(2,numero):
        if (numero % i == 0):
            cont += 1
            break
        return cont == 0

lista_valores.barrido()
print()
cont = 0
while cont <  lista_valores.size():
    if es_primo(lista_valores.barrido()):
        lista_valores.delete()
    else:
        cont += 1
print()
lista_valores.barrido()
