import mariadb

class Database_Watcher(object):
    def __init__(self):
        pass
        
    def read_data(self,SQL,connectiondata):

        Server = connectiondata[0]
        Username = connectiondata[1]
        Password = connectiondata[2]
        Databasename = connectiondata[3]
        try:
            conn = mariadb.connect(user=Username,password=Password,host=Server,port=3306,database=Databasename)
            print("Information: Connected to Database: "+str(Databasename)+" with User: "+str(Username))
        except mariadb.Error as e:
            print(f"Error: Cant connecting to MariaDB Platform: {e}")
            sys.exit(1)
        cur = conn.cursor()
        print("Information: SQL command is executed: "+str(SQL))
        cur.execute(SQL) 
        Ergebnis1 = cur
        Ergebnis = []
        for a in Ergebnis1:
            Ergebnis.append(a)
        conn.close()
        print("Information: Connection to Database closed")
        return(Ergebnis)

    def write_data(self,SQL,connectiondata):
        Server = connectiondata[0]
        Username = connectiondata[1]
        Password = connectiondata[2]
        Databasename = connectiondata[3]
        try:
            conn = mariadb.connect(user=Username,password=Password,host=Server,port=3306,database=Databasename)
            print("Information: Connected to Database: "+str(Databasename)+" with User: "+str(Username))
        except mariadb.Error as e:
            print(f"Error: Cant connecting to MariaDB Platform: {e}")
            sys.exit(1)
        cur = conn.cursor()
        print("Information: SQL command is executed: "+str(SQL))
        cur.execute(SQL) 
        conn.commit() 
        conn.close()
        print("Information: Connection to Database closed")
        