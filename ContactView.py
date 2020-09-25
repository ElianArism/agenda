# Vista de Contacto. 

class ContactView:
    #Inicializa las opciones. 
    def __init__(self): 
        self.op1 = 'Listar Contactos'
        self.op2 = 'Agregar Contacto'
        self.op3 = 'Buscar Contacto'
        self.op4 = 'Editar Contacto'
        self.op5 = 'Eliminar Contacto'
        self.op6 = 'Cerrar Agenda'

   #Muestra el menu.  
    def Menu(self):         
        print('-------------- Menu Contacto ----------------')
        print(f'1--{self.op1}')
        print(f'2--{self.op2}')
        print(f'3--{self.op3}')
        print(f'4--{self.op4}')
        print(f'5--{self.op5}')
        print(f'6--{self.op6}')
        print(f'============================================')

        return int(input())
    
    #Imprime todas las respuestas. 
    def Response(self, res):
        print("---------RESULTADOS-------------")
        for r in res:
            print(r)

    #Metodo utilizado para pedir datos por consola. 
    def Request(self,*args):
        print("Se precisan estos datos para continuar: ")
        out = dict()
        for r in args:
            out[r] = input(r+" ")
        return out

    #Metodo que se ejecuta si se envia un id invalido. 
    def notFound(self): 
        print('No se encontro el id de la agenda buscada.')
    
    #Este metodo se utiliza exclusivamente para editar contactos. 
    def update(self): 
        v = int(input('Que campo de su contacto desea editar? \n1. nombre\n2. telefono\n3. Email\n4. Todo\nIngrese una opcion: '))
        n = dict()
        try:
            if(v == 1): 
                n['nombre'] = input('ingrese el nombre: ')
                n['flag'] = 1
            elif(v == 2): 
                n['telefono'] = int(input('ingrese el telefono: ')) 
                n['flag'] = 2
            elif(v == 3): 
                n['email'] = input('ingrese el email: ')
                n['flag'] = 3
            elif( v == 4): 
                n = self.Request('nombre', 'telefono', 'email')
                n['flag'] = 4 
            elif(v > 4 or v < 1): 
                print('Opcion no valida.')
                return None
        except: 
            print('Ingreso datos incorrectos en algun campo.') 
            return None
        
        return n 

    #Mensaje de despedida.
    def byeMSG(self): 
        print('Adios.')
    
    #Este metodo se ejecuta cuando se desea eliminar un contacto especifico.
    def deleteMSG(self): 
        print('Estos son los registros encontrados con ese nombre, por seguridad, escriba el dni del contacto que desea eliminar: ')
        return self.Request('dni')