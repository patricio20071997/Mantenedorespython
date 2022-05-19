import pymysql
from claseCliente import Cliente

def conectar():
    try:
        conexion = pymysql.connect(host='localhost', user='root', passwd='', db='prueba')
    except:
        print("Error de conexion")
    return conexion

def insertar(cliente):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO cliente (rut,nombre,correo,pass) VALUES (%s,%s,%s,%s);"
            cursor.execute(consulta,(cliente.rut,cliente.nombre,cliente.correo,cliente.passw))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar",ex)        
    conexion.close()    



def consultar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM cliente")
            auxCliente = cursor.fetchall()
            for cli in auxCliente:
                print(cli)
            return auxCliente    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Ocurrio un error en la consulta", ex)
    conexion.close()  


def buscar(auxRut):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT rut, nombre, correo, pass FROM cliente WHERE rut = %s;"
            cursor.execute(consulta,(auxRut))
            auxCliente = cursor.fetchall()
            for cli in auxCliente:
                print(cli)
            return auxCliente    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Ocurrio un error en la busqueda", ex)
    conexion.close()  


def actualizar(cliente):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE cliente SET nombre = %s, correo = %s, pass = %s WHERE rut = %s ;"
            cursor.execute(consulta,(cliente.nombre,cliente.correo,cliente.passw,cliente.rut))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al actualizar",ex)        
    conexion.close()


def eliminar(auxRut):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM cliente WHERE rut = %s ;"
            cursor.execute(consulta, (auxRut))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al eliminar",ex)        
    conexion.close()

#programa principal
conectar()
print("Conectado")





#print("Buscar Cliente")
#buscar("111")
#auxCliente = Cliente("1111","ppp","dfd","123")
#insertar(auxCliente)
#auxCliente = Cliente("111","Chocolate","aa","111")
#actualizar(auxCliente)
#eliminar("1")

consultar()