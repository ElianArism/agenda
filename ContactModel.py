from ConnectDB import DB

# Modelo de Contacto. 
class Contact: 
    __DB = DB(name = 'AgendaDB')
    __tableName = 'Contacto'


    #Cada instancia de contacto debe contar con estas propiedades. 
    def __init__(self, dni , name, email, tel):
        self.__dni = dni
        self.__name = name
        self.__email = email 
        self.__tel = tel 

    #Trae todos los contactos de la base de datos. 
    @classmethod
    def getAllContacts(cls, id): 
        qry = "SELECT * FROM "+Contact.__tableName+" WHERE "+Contact.__tableName+".id_agenda = "+ str(id)
        return Contact.__DB.Execute(qry)

    #Trae un contacto especifico de la base de datos. 
    @classmethod
    def getContact(cls, id, contactName): 
        qry = "SELECT * FROM "+Contact.__tableName+" WHERE "+Contact.__tableName+".id_agenda = "+ str(id)+" AND "+Contact.__tableName+".nombre = "+"'"+contactName+"'" 
        return Contact.__DB.Execute(qry)
   
    #Crea un nuevo contacto en la base de datos. 
    def createContact(self, id):
        qry = "INSERT INTO " +Contact.__tableName+ "(dni, id_agenda, nombre, telefono, email) VALUES (?,"+str(id)+",?,?,?)"
        vls = (self.__dni, self.__name, self.__email, self.__tel)
        return Contact.__DB.Execute(qry,vls)
        
    #Edita/Actualiza un contacto en la base de datos dependiendo de las propiedades que contenga el diccionario data. 
    @classmethod
    def updateContact(cls, nombre, data): 
        if(data['flag'] == 4):
            qry = f"UPDATE {Contact.__tableName} SET {Contact.__tableName}.nombre = '{str(data['nombre'])}', {Contact.__tableName}.telefono = {data['telefono']}, {Contact.__tableName}.email = '{str(data['email'])}' WHERE {Contact.__tableName}.nombre = '{str(nombre)}' " 
        elif(data['flag'] == 1): 
            qry = f"UPDATE {Contact.__tableName} SET {Contact.__tableName}.nombre = '{str(data['nombre'])}' WHERE {Contact.__tableName}.nombre = '{str(nombre)}' " 
        elif(data['flag'] == 2): 
            qry = f"UPDATE {Contact.__tableName} SET {Contact.__tableName}.telefono = {data['telefono']} WHERE {Contact.__tableName}.nombre = '{str(nombre)}' " 
        elif(data['flag'] == 3):
            qry = f"UPDATE {Contact.__tableName} SET {Contact.__tableName}.email = '{str(data['email'])}' WHERE {Contact.__tableName}.nombre = '{str(nombre)}' " 
        
        return Contact.__DB.Execute(qry)

    #Este metodo se encarga de eliminar todos los contactos vinculados a una agenda en la base de datos, o elimina un contacto especifico si la propiedad dni es enviada como parametro. 
    @classmethod
    def deleteContacts(cls, id_agenda, data = None): 
        
        if(data == None):
            qry = f"DELETE FROM {Contact.__tableName} WHERE {Contact.__tableName}.dni = {data['dni']} AND {Contact.__tableName}.id_agenda = {id_agenda} "
        else: 
            qry = f"DELETE FROM {Contact.__tableName} WHERE {Contact.__tableName}.id_agenda = {id_agenda}"
            
        Contact.__DB.Execute(qry)

        