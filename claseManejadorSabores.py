import csv
from ClaseSabor import Sabor
class ManejadorSabores:
    __listaS=[]
    
    
    def __init__(self):
        self.__listaS=[]
        
        
    def agregarSabor(self,unSabor):
        self.__listaS.append(unSabor)
        
        
    def crear_sabor(self):
        archivo=open("C:\\Users\\chili\\POO archivos\\sabores.csv")
        reader=csv.reader(archivo,delimiter=",")
        band=True
        for fila in reader:
            if band:
                band= not band
            else:
                Id=fila[0]
                ingrediente=fila[1]
                nombre=fila[2]
                unSabor=Sabor(Id,ingrediente,nombre)
                self.agregarSabor(unSabor)
        archivo.close()
        
        
        
    def __str__(self):
        s=""
        for sabore in self.__listaS:
            s+=str(sabore)+"\n"
            
        return s
                
   
    def get_sabor(self):
        return self.__listaS
    

    

            
            
            