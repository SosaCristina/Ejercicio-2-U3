from claseManejadorSabores import ManejadorSabores
from ClaseHelado import Helado
from ClaseSabor import Sabor
class ManejadorHelados:
    __listaH: list
    
    
    
    
    def __init__(self):
        self.__listaH=[]
        
        
    def agregarHelado(self,helado):
        self.__listaH.append(helado)
        
        
        
    def crear_venta(self,sabores):
        gramos=input("ingrese gramos")
        precio=input("ingrese precio")
        cantidad=int(input("Ingrse la cantidad de sabores"))
        print("Mostrar sabores de helados")
        print(sabores)
        unHelado=Helado(gramos,precio)
        for i in range(cantidad):
            Id=input("ingrese id del sabor")
            unsabor=sabores.get_sabor()[int(Id)-1]
            unHelado.addSabor(unsabor)
        self.agregarHelado(unHelado)
        del unHelado
        
        
    def mostrarHeladosVendidos(self):
        for helado in self.__listaH:
            print(helado)
    
            
    def maspedido (self,unSabor):
        datos={}
        contadores=[]
        for i in range (len(unSabor.get_sabor())):
            datos={"cont":0,"id":i+1}
            contadores.append(datos)
        
        for i in range (len(contadores)):
            for j in range (len(self.__listaH)):
                helado=self.__listaH[j]
                contadores[i]["cont"]+=int(helado.obtener_sabor(contadores[i]["id"]))


        contadores.sort(key=lambda x: x["cont"],reverse=True)
        #print("ORDENADO")
        #print(contadores)
        print("LOS SABORES MAS VENDIDOS SON:")
        for i in range(5):
            idC=contadores[i]["id"]
            
            sabor=unSabor.get_sabor()[int(idC)-1]
            print("Uno de los sabores mas vendidos es: {}".format(sabor.get_nombre()))    



    def total_gramos (self):
        total=0
        id=int(input("Ingrese Id que desee saber el total de gramos vendidos:"))
        for lista in self.__listaH:
            total+=lista.calcular_gramos(id)
        print("El total de gramos vendidos es:",total)

    def tipo (self):
        gr=int(input("Ingresar un tipo de helado: "))
        print("Los sabores vendidos en ese tamaño son: ")
        for lista in self.__listaH:
            if (int(gr) == int(lista.get_gramos())):
                print(lista.get_sabor())

    def importe (self):
        cont1=0
        cont2=0
        cont3=0
        cont4=0
        cont5=0
        for lista in self.__listaH:
            if int(lista.get_gramos())==int(100):
                cont1+=int(lista.get_importe())
            else:
                if int(lista.get_gramos())==int(150):
                    cont2+=int(lista.get_importe())
                else:
                    if int(lista.get_gramos())==int(250):
                        cont3+=int(lista.get_importe())
                    else:
                        if int(lista.get_gramos())==int(500):
                            cont4+=int(lista.get_importe())
                        else:
                            if int(lista.get_gramos())==int(1000):
                               cont5+=int(lista.get_importe())
        print("El importe total del tipo de helado (100) es:",cont1)
        print("El importe total del tipo de helado (150) es:",cont2)
        print("El importe total del tipo de helado (250) es:",cont3)
        print("El importe total del tipo de helado (500) es:",cont4)
        print("El importe total del tipo de helado (1000) es:",cont5)
            

                
            






            
        
        
        