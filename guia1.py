
#Ejercicio 5
romano = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c':100, 'd':500, 'm':1000 }

def convert_romano_to_dec(numero_romano):
    if len(numero_romano) == 1:
        return romano[numero_romano]
    else:
        if romano[numero_romano[0]]>= romano[numero_romano[1]]:
            return romano[numero_romano[0]] + convert_romano_to_dec(numero_romano[1:])
        else:
            return  - romano[numero_romano[0]] + convert_romano_to_dec(numero_romano[1:])

print(convert_romano_to_dec('ix'))

#Ejercicio 22
mochila = ['Comida', 'rifle bláster', 'Sable de luz', 'otro']

def usar_fuerza(mochila, pos=0):
     if(pos< len(mochila)):
         if(mochila[pos] == 'Sable de luz'):
             return pos+1
         else:
             return usar_fuerza(mochila, pos+1)
     else:
         return -1

cantidad=usar_fuerza(mochila)
if cantidad == -1:
    print("No se encontro un sable de luz")
else:
    print("la cantidad de objetos necesarios para encontrar el sable de luz fue", cantidad)
