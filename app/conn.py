import mysql.connector

class Connection:
    @staticmethod
    def createConn():
        mydb = mysql.connector.connect(
            host="db",
            user="root",
            password='root',
            database="RI",
        )

        return mydb
    
    @staticmethod
    def insertDB(mydb, nome, email):

        mycursor = mydb.cursor()
        print(nome, email)
        sql = f'INSERT INTO Usuario (user_nome, user_email) VALUES ("{nome}", "{email}");'
        mycursor.execute(sql)

        mydb.commit()

        return