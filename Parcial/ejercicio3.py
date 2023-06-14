from pila import Pila
class Bitacora():

    def __init__(self, planeta, captura, recompensa):
        self.planeta = planeta
        self.captura = captura
        self.recompensa = recompensa

    def __str__(self):
        return f'{self.planeta} {self.captura} {self.recompensa} '

informacion = [
    {'planet':'Tatooine','caza': 'Jabba the Hutt','money': 100},
    {'planet':'Bespin','caza': 'Han Solo','money': 160},
    {'planet':'Bespin','caza': 'Lando Calrissian','money': 200},
    {'planet':'Endor','caza': 'Ewoks','money': 50},
    {'planet':'Naboo','caza': 'Padmé Amidala','money': 350},
    
]
pila=Pila()
for info in informacion:
    pila.push(Bitacora(info['planet'],
                       info['caza'],
                       info['money'],))
pilaAux= Pila()
#punto A
for i in range (pila.size()):
    data=pila.pop()
    pilaAux.push(data)
    print(data.planeta)

for i in range (pilaAux.size()):
    pila.push(pilaAux.pop())
    
#punto b
mision = 1
credito=0
for i in range (pila.size()):
    data=pila.pop()
    credito += data.recompensa
    if data.captura == 'Han Solo':
        print(f"se encontro a Han solo en la mision {mision} y en el planeta {data.planeta}")
    mision +=1    
    # cont2+=1
print('la cantidad de creditos reunidos es', credito)    

    


