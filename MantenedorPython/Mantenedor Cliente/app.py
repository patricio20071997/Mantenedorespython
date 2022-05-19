#Este es el programa de arranque
import mantenedorCliente
import claseCliente
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

#Se rutea el home

@app.route('/')

def Index():
   #return 'Holi'
   datos = mantenedorCliente.consultar()
   return render_template('MantenedorCliente.html',clientes=datos)
   #return render_template('MantenedorCliente.html')


@app.route('/mantenedor', methods = ['POST'])

def mantenedor():
   if request.method == 'POST':
      #Insertar
      try:
         auxBotonInsertar = request.form['btoInsertar']
         if auxBotonInsertar == 'Insertar':
            auxRut = request.form['txtRut']
            auxNombre = request.form['txtNombre']
            auxCorreo = request.form['txtCorreo']
            auxPass = request.form['txtPass']
            auxCliente = claseCliente.Cliente(auxRut,auxNombre, auxCorreo, auxPass)
            mantenedorCliente.insertar(auxCliente)
            print('Datos guardados')
            #flash('datos guardados')
      except:
         print('Datos no guardados')
     #Actualizar
      try:
         auxBotonActualizar = request.form['btoActualizar']
         if auxBotonActualizar == 'Actualizar':
            auxRut = request.form['txtRut']
            auxNombre = request.form['txtNombre']
            auxCorreo = request.form['txtCorreo']
            auxPass = request.form['txtPass']
            auxCliente = claseCliente.Cliente(auxRut,auxNombre, auxCorreo, auxPass)
            mantenedorCliente.actualizar(auxCliente)
            print('Datos Actulizados')
            #flash('datos guardados')
      except:
         print('Datos no Actulizados')
      #Eliminar
      try:
         auxBotonEliminar = request.form['btoEliminar']
         if auxBotonEliminar == 'Eliminar':
            auxRut = request.form['txtRut']
            mantenedorCliente.eliminar(auxRut)
            print('Datos Eliminados')
            #flash('datos guardados')
      except:
         print('Datos no Eliminados')

      return redirect(url_for('Index'))


      

if __name__ == '__main__':
   app.run(port=3000,debug=True)