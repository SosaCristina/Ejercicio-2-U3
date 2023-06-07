class Sabor:
    __idSabor: int
    __ingredientes: str
    __nombre: str
    
    
    def __init__(self,Id,ingrediente,nombre):
        self.__idSabor=Id
        self.__ingredientes=ingrediente
        self.__nombre=nombre
        
        
    def  __str__(self):
        return ("Id del sabor: {}, ingredientes: {}, Nombre del sabor: {}".format(self.__idSabor,self.__ingredientes,self.__nombre))
    
    def getid(self):
        return self.__idSabor
    def get_nombre(self):
        return self.__nombre