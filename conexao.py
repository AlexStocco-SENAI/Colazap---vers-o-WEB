import mysql.connector

class Conexao():
    def conectar():
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="equipe",
            password="123456789",
            database="colazap"
            )
        
        return mydb