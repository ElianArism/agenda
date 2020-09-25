import pyodbc

#Toda la configuracion correspondiente a la base de datos esta alojada en este archivo. 
class DB: 
    def __init__(self, name, sv = 'DESKTOP-186D8IR\\SQLEXPRESS', driver = 'SQL Server Native Client 11.0'): 
        self.__name = name    
        self.__sv = sv 
        self.__driver = driver
        self.__conection = None
        self.__data = None
    
    def Connect(self): 
        self.__conection = pyodbc.connect("DRIVER={"+self.__driver+"};"
                                            "Server="+self.__sv+";"
                                            "DATABASE="+self.__name+";"
                                            "Trusted_Connection=yes;")
    
    def Cursor(self):
        self.__cursor = self.__conection.cursor()

    def Commit(self, qry): 
        isSelect = qry.count('SELECT') 
        if(isSelect == 0): 
            self.__conection.commit()
    
    def Close(self): 
        self.__conection.close()
    
    def getData(self, qry): 
        isSelect = qry.count('SELECT') 
        if(isSelect > 0): 
            self.__data = self.__cursor.fetchall()
        
    def Query(self, qry, vls = None):
        if(vls):
            self.__cursor.execute(qry, vls) 
        else: 
            self.__cursor.execute(qry)

    def Execute(self, qry, vls = None): 
        self.Connect()
        self.Cursor()
        self.Query(qry, vls)
        self.Commit(qry)
        self.getData(qry)
        self.Close()

        return self.__data
    