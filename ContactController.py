from ContactModel import Contact
from ContactView import *

# Controlador de contacto. 
class ContactController: 
    #Cada nueva instancia del controlador inicializa el id de la agenda correspondiente y una nueva instancia de la vista. 
    def __init__(self, id_agenda): 
        self.__id_agenda = id_agenda
        self.__newView = ContactView()

    #Direcciona la peticion del usuario al metodo correspondiente. 
    def Home(self): 
        option =  self.__newView.Menu()
        if(option == 1): 
            self.contactList()
        elif(option == 2): 
            self.createContact()
        elif(option == 3): 
            self.findContacts()
        elif(option == 4): 
            self.updateContact()
        elif(option == 5): 
            self.deleteContact()
        elif(option == 6):
            self.closeAgenda()
        
    #Lista todos los contactos. 
    def contactList(self): 
        contacts = Contact.getAllContacts(self.__id_agenda)
        self.__newView.Response(contacts)
        return self.Home()

    #Encuentra un contacto especifico. 
    def findContacts(self): 
        data = self.__newView.Request('nombre_contacto') 
        contacts = Contact.getContact(self.__id_agenda, data['nombre_contacto'])
        if(len(contacts) < 1): 
            self.__newView.notFound()
        else:     
            self.__newView.Response(contacts) 
        
        return self.Home() 

    #Crea un nuevo contacto. 
    def createContact(self): 
        data = self.__newView.Request('dni', 'nombre', 'telefono', 'email')
        newContact = Contact(data['dni'], data['nombre'], data['telefono'], data['email'])
        newContact.createContact(self.__id_agenda)

        return self.Home()

    #Editar un contacto. 
    def updateContact(self):
        data = self.__newView.Request('nombre') 
        Oldcontact = Contact.getContact(self.__id_agenda, data['nombre'])
        self.__newView.Response(Oldcontact)
        updateContact = self.__newView.update()
        if(updateContact != None): 
            Contact.updateContact(data['nombre'], updateContact)

        return self.Home()

    #Eliminar un contacto. 
    def deleteContact(self): 
        data = self.__newView.Request('nombre') 
        listContact = Contact.getContact(self.__id_agenda, data['nombre'])
        self.__newView.Response(listContact)
        data = self.__newView.deleteMSG()
        Contact.deleteContacts(self.__id_agenda, data)
        
        return self.Home()

    #Cierra la agenda.         
    def closeAgenda(self): 
        self.__newView.byeMSG()
