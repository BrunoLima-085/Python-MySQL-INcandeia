import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.conn = self.connect()

    def connect(self):
        try:
            conn = mysql.connector.connect(
                host = "Localhost",
                user = "root",
                password = "MySQL",
                database = "INcandeia"
            )
            if conn.is_connected():
                print("Conectado ao banco de dados com sucesso!!!")
                return conn
        except Error as e:
            print("Erro ao conectar ao banco de dados:", e)

    def execute(self, query, params=None, fetch=None):
        try:
            with self.conn.cursor(dictionary=True) as cursor:
                cursor.execute(query, params or ())
                if fetch == "one": 
                    return cursor.fetchone()
                if fetch == "all": 
                    return cursor.fetchall()
                self.conn.commit()
                return True
        except Error as e:
            print("Erro", e)
            return None
        
    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Conexão fechada com sucesso!!!")          


    