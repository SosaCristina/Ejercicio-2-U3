from ClaseSabor import Sabor
class Helado:
    __gramos: int
    __precio: int
    __listasabores: list
    
    def addSabor(self,sabor):
        self.__listasabores.append(sabor)
        
    def __init__(self, gramos, precio, sabor=None):
        self.__gramos=gramos
        self.__precio=precio
        self.__listasabores=[]
        if sabor != None:
            self.addSabor(sabor)
        
        
        
    def __str__(self):
        s=("Gramos {}, precio {}\n".format(self.__gramos,self.__precio))
        for sabore in self.__listasabores:
            s+=str(sabore)+"\n"
            
        return s
    
    def get_sabor(self):
        for sabor in self.__listasabores:
            print(sabor.get_nombre())

    def get_gramos(self):
        return self.__gramos
    
    def get_importe(self):
        return self.__precio
    
    def obtener_sabor(self,id):
        cont=0
        for sabor in self.__listasabores :
            if int(sabor.getid())== int(id):
                cont+=1
        return cont    
    

    def calcular_gramos(self,id):
        cont=0
        i=0
        bandera=False
        while i< len(self.__listasabores) and not bandera:
            if (int(id) == int(self.__listasabores[i].getid())):
                cont+= int(self.__gramos) / int(len(self.__listasabores))
                bandera=True
            else:
                i+=1
        return cont            


    

    
        


        
        
    
        