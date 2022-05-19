import pymysql
from claseServicio import Servicio



def conectar():
    try:
        conexion = pymysql.connect(host='localhost', user='root', passwd='', db='prueba')
    except:
        print("Error de conexion")
    return conexion



def insertar(servicio):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO servicio (cod,nombre,valor) VALUES (%s,%s,%s);"
            cursor.execute(consulta,(servicio.cod,servicio.nombre,servicio.valor))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar",ex)        
    conexion.close()    



def consultar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM servicio")
            auxServicio = cursor.fetchall()
            for ser in auxServicio:
                print(ser)
            return auxServicio    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Ocurrio un error en la consulta", ex)
    conexion.close()  



def buscar(auxCod):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT cod, nombre, valor FROM servicio WHERE cod = %s;"
            cursor.execute(consulta,(auxCod))
            auxServicio = cursor.fetchall()
            for ser in auxServicio:
                print(ser)
            return auxServicio    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Ocurrio un error en la busqueda", ex)
    conexion.close()  



def actualizar(servicio):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE servicio SET nombre = %s, valor = %s WHERE cod = %s ;"
            cursor.execute(consulta,(servicio.nombre,servicio.valor,servicio.cod))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al actualizar",ex)        
    conexion.close()



def eliminar(auxCod):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM servicio WHERE cod = %s ;"
            cursor.execute(consulta, (auxCod))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al eliminar",ex)        
    conexion.close()




conectar()
print("Conectado")
consultar()
#buscar("000")
#auxMecanico = Mecanico("000","Chocolate","aa","111","mecanico")
#actualizar(auxMecanico)
#consultar()
#eliminar("000")