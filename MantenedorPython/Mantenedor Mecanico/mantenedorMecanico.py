import pymysql
from claseMecanico import Mecanico



def conectar():
    try:
        conexion = pymysql.connect(host='localhost', user='root', passwd='', db='prueba')
    except:
        print("Error de conexion")
    return conexion



def insertar(mecanico):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO mecanico (rut,nombre,correo,pass, cargo) VALUES (%s,%s,%s,%s,%s);"
            cursor.execute(consulta,(mecanico.rut,mecanico.nombre,mecanico.correo,mecanico.passw,mecanico.cargo))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar",ex)        
    conexion.close()    



def consultar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM mecanico")
            auxMecanico = cursor.fetchall()
            for mec in auxMecanico:
                print(mec)
            return auxMecanico    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Ocurrio un error en la consulta", ex)
    conexion.close()  



def buscar(auxRut):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT rut, nombre, correo, pass, cargo FROM mecanico WHERE rut = %s;"
            cursor.execute(consulta,(auxRut))
            auxMecanico = cursor.fetchall()
            for mec in auxMecanico:
                print(mec)
            return auxMecanico    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Ocurrio un error en la busqueda", ex)
    conexion.close()  



def actualizar(mecanico):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE mecanico SET nombre = %s, correo = %s, pass = %s, cargo = %s WHERE rut = %s ;"
            cursor.execute(consulta,(mecanico.nombre,mecanico.correo,mecanico.passw,mecanico.cargo,mecanico.rut))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al actualizar",ex)        
    conexion.close()



def eliminar(auxRut):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM mecanico WHERE rut = %s ;"
            cursor.execute(consulta, (auxRut))
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