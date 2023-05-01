from pila import Pila
from random import randint

stack = Pila()
#! carga
for i in range(10):
    valor = randint(0, 20)
    print('valor generado', valor)
    stack.push(valor)


contador_coincidencias = 0  
numero_busca = input("ingrese un numero entre 0 y 20 ") 
numero_busca = int(numero_busca)
while stack.size() > 0:  
    valore = stack.pop() 
    if valore == numero_busca:
        contador_coincidencias +=1
     
print(f'la cantidad de veces que se repite es{contador_coincidencias}')        