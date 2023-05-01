def sumas(numero):
    """resuleve el factorial de un numero n de manera iterativo"""
    suma = 0
    for i in range(1, numero+1):
        suma = suma + i
        #print("la suma hasta ahora es", suma)
    return suma
#print("la suma de esos numero son", sumas(5))

def sumarecursiva(numero):
    """devuelve la suma entre 0 y un numero positivo"""
    # print('valor devariable', numero)
    if numero == 0:
        return numero
    else:
        return numero + sumarecursiva(numero-1)
#print("la suma de esos numero son", sumarecursiva(3))     

def potencia(base, exponente):
    """potencia con una base y exponentes dados"""
    # print('valor devariable', numero)
    if exponente == 0:
        return 1
    if exponente == 1:
        return base
    else:
        return base * potencia(base,exponente-1)

#print("la potencia es", potencia(3,3))

def inversion(palabra):
    """devuelve una palabra invertida"""
    if len(palabra) == 0:
        return ""
    else:
        return palabra[-1] + inversion(palabra[0:-1])
    
          
#print(inversion("equis de")) 

def sumafraccion(numero):
    """suma los valores desde 1, 1/2, 1/3 ... hasta 1/n"""
    if numero == 1:
        return 1
    else:
        return (1/numero) + sumafraccion(numero-1)
    
#print(sumafraccion(10))    

