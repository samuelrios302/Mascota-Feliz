import mysql.connector
from mysql.connector import Error

class Conexion_MySQL:

    _conexion = None

    def __new__(cls):
        if cls._conexion is None:
            try:
                cls._conexion = mysql.connector.connect (
                    username = "qfqv5eyt372yreiv",
                    password = "o5nyeiaueqtzwtql",
                    host = "l3855uft9zao23e2.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
                    port = "3306",
                    database = "kec6oj1sn5kdspby")

                if cls._conexion.is_connected():
                    print("Conexion exitosa a la base de datos!")

            except Error as e:
                print(f"ha ocurrido un error de conexion: {e}")
        
        return cls._conexion

conexion1 = Conexion_MySQL()