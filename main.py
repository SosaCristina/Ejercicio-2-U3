from claseManejadorHelados import ManejadorHelados
from claseManejadorSabores import ManejadorSabores
from ClaseHelado import Helado
from ClaseSabor import Sabor

if __name__=="__main__":
  
    unSabor=ManejadorSabores()
    unSabor.crear_sabor()
    #print(unSabor)
    unHelado=ManejadorHelados()
    unHelado.crear_venta(unSabor)
    unHelado.crear_venta(unSabor)
    unHelado.crear_venta(unSabor)
    #unHelado.mostrarHeladosVendidos()
    #unHelado.maspedido(unSabor)
    #unHelado.total_gramos()
    #unHelado.tipo()
    unHelado.importe()
