#Vista de agenda. 
class AgendaView: 
    #Inicializa todas las opciones disponibles. 
    def __init__(self): 
        self.op1 = 'Listar Agendas'
        self.op2 = 'Seleccionar Agenda'
        self.op3 = 'Nueva Agenda'
        self.op4 = 'Eliminar Agenda'
        self.op5 = 'Cerrar Agenda'
    
    #Menu. 
    def Menu(self): 
        print('-------------- Menu Gestor Agendas ----------------')
        print(f'1--{self.op1}')
        print(f'2--{self.op2}')
        print(f'3--{self.op3}')
        print(f'4--{self.op4}')
        print(f'5--{self.op5}')
        print(f'==================================================')

        return int(input())

    #Metodo encargado de mostrar todos los resultados. 
    def Response(self, res):
        print("---------RESULTADOS-------------")
        for r in res:
            print(r)

    #Metodo encargado de pedirle datos al usuario. 
    def Request(self,*args):
        print("Se precisa esta informacion")
        out = dict()
        for r in args:
            out[r] = input(r+" ")
        return out

    #Mensaje de notificacion para cuando una agenda es eliminada.
    def DeletedMSG(self, boolean):
        if(boolean): 
            print('Se elimino satisfactoriamente la agenda.')
        else: 
            self.notFound()

    #Notificacion cuando no existe agenda vinculada con un id suministrado. 
    def notFound(self): 
        print('No se encontro el id de la agenda buscada')
    
    #Mensaje de despedida. 
    def ByeMSG(self): 
        print('Adios, ten un buen dia')