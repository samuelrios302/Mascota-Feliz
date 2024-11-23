import mysql.connector
from mysql.connector import Error

class Conexion_MySQL:

    _conexion = None

    def __new__(cls):
        if cls._conexion is None:
            try:
                cls._conexion = mysql.connector.connect (
                    username = "ezz3ttl39o1f7vel",
                    password = "xyw6i2w9id949cca",
                    host = "zj2x67aktl2o6q2n.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
                    port = "3306",
                    database = "jsolm72hf742hg3y"
                )
            except Error as e:
                print(f"ha ocurrido un error de conexion: {e}")
        
        return cls._conexion

conexion1 = Conexion_MySQL()

#Usuario: ezz3ttl39o1f7vel
#Contraseña: xyw6i2w9id949cca
#Host: zj2x67aktl2o6q2n.cbetxkdyhwsb.us-east-1.rds.amazonaws.com
#Port: 3306
#Database: jsolm72hf742hg3y