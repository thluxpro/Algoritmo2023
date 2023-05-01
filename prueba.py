lista_num = [10, 2, -3, 10, None]
lista_num.append(0)
lista_num.append(50)
# lista_num.remove(10)
lista_num.insert(1, 11)
# lista_num.sort()
lista_num[3] = 6
print(lista_num[3])
print(lista_num, len(lista_num))
lista_num.pop(2)
# print(lista_num, len(lista_num))

lista_num.reverse()
for i in range(len(lista_num)):
    print('elemento en indice', i, lista_num[i])