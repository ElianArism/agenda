from ConnectDB import DB

#Modelo de agenda. 
class Agenda: 
    __DB = DB(name = 'AgendaDB')
    __tableName = 'Agenda' 

    #Cada agenda se inicializa con un id, y un propietario. 
    def __init__(self,id, owner):
        self.__id = id 
        self.__owner = owner  

    #Guarda una nueva agenda en la base de datos. 
    def save(self):
        query = "INSERT INTO " +Agenda.__tableName+ "(id_agenda,propietario) VALUES (?,?)"
        values = (self.__id, self.__owner)
        return Agenda.__DB.Execute(query,values)
    
    #Trae todas las agendas desde la base de datos. 
    @classmethod
    def getAllAgendas(cls):
        query = "SELECT * FROM "+ Agenda.__tableName
        return Agenda.__DB.Execute(query)

    #Busca una agenda en la base de datos. 
    @classmethod 
    def findAgenda(cls, id): 
        query = "SELECT * FROM "+Agenda.__tableName+" WHERE "+Agenda.__tableName+".id_agenda = "+ str(id) 
        return Agenda.__DB.Execute(query)

    #Elimina una agenda de la base de datos. Si se elimina una agenda tambien se borraran todos los contactos almacenados en ella.  
    @classmethod
    def deleteAgenda(cls, id):
        query = "DELETE FROM "+Agenda.__tableName+" WHERE "+Agenda.__tableName+".id_agenda = "+ str(id)
        return Agenda.__DB.Execute(query)