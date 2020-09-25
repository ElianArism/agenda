from AgendaModel import Agenda
from AgendaView import *

from ContactModel import Contact
from ContactController import ContactController

#Controlador de agenda. 
class AgendaController: 
    
    #Cada instancia del controlador inicializa una nueva vista y un id.  
    def __init__(self): 
        self.__ViewNew = AgendaView()
        self.__id  = None

    #Home redirecciona las peticiones del usuario a los metodos correspondientes. 
    def Home(self):
        option = self.__ViewNew.Menu()
        if option == 1:
            self.ShowAll()    
        elif(option == 2):
            self.selectAgenda()
        elif option == 3: 
            self.addAgenda()
        elif option == 4:
            self.deleteAgenda()
        elif option == 5:
            self.closeAgenda()

    #Muestra todas las agendas disponibles.
    def ShowAll(self): 
        res = Agenda.getAllAgendas()
        self.__ViewNew.Response(res)           
        self.Home()
    
    #Crea una nueva agenda. 
    def addAgenda(self): 
        owner = self.__ViewNew.Request('id', 'propietario')
        newAgenda = Agenda(owner['id'], owner['propietario'])

        newAgenda.save()   
        self.Home()  

    #Selecciona una agenda para obtener acceso a los contactos almacenados en la misma y poder operar con ellos. 
    def selectAgenda(self): 
        data = self.__ViewNew.Request('id')
        id = int(data['id']) 
        self.__id = id
        self.__contactController = ContactController(self.__id)
        agenda = Agenda.findAgenda(id)      

        if(len(agenda) < 1): 
            self.__ViewNew.notFound()    
            return self.Home()
                   
        self.__ViewNew.Response(agenda)
        self.__contactController.Home()
        self.Home()        
    
    #Elimina una agenda. 
    def deleteAgenda(self): 
        data = self.__ViewNew.Request('id')
        id = data['id']
        lisst = Agenda.findAgenda(id)
        
        if(len(lisst) > 0): 
            Contact.deleteContacts(id)
            Agenda.deleteAgenda(id)
            self.__ViewNew.DeletedMSG(True)
         
        self.__ViewNew.DeletedMSG(False)
        self.Home()

    #Cierra la agenda.
    def closeAgenda(self): 
        return self.__ViewNew.ByeMSG()