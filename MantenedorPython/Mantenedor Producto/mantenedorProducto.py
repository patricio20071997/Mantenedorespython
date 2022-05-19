import pymysql
from claseProducto import Producto



def conectar():
    try:
        conexion = pymysql.connect(host='localhost', user='root', passwd='', db='prueba')
    except:
        print("Error de conexion")
    return conexion



def insertar(producto):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO producto (cod,nombre,valor,stock) VALUES (%s,%s,%s,%s);"
            cursor.execute(consulta,(producto.cod,producto.nombre,producto.valor,producto.stock))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar",ex)        
    conexion.close()    



def consultar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM producto")
            auxProducto = cursor.fetchall()
            for pro in auxProducto:
                print(pro)
            return auxProducto    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Ocurrio un error en la consulta", ex)
    conexion.close()  



def buscar(auxRut):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT cod, nombre, valor, stock FROM producto WHERE cod = %s;"
            cursor.execute(consulta,(auxRut))
            auxProducto = cursor.fetchall()
            for pro in auxProducto:
                print(pro)
            return auxProducto    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("Ocurrio un error en la busqueda", ex)
    conexion.close()  



def actualizar(producto):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE producto SET nombre = %s, valor = %s, stock = %s WHERE cod = %s ;"
            cursor.execute(consulta,(producto.nombre,producto.valor,producto.stock,producto.cod))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al actualizar",ex)        
    conexion.close()



def eliminar(auxCod):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM producto WHERE cod = %s ;"
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