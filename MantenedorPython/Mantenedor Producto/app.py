#Este es el programa de arranque
import mantenedorProducto
import claseProducto
from flask import Flask, render_template, request, flash, redirect, url_for



app = Flask(__name__)

#Se rutea el home

@app.route('/')

def Index():
   #return 'Holi'
   datos = mantenedorProducto.consultar()
   return render_template('MantenedorProducto.html',productos=datos)
   #return render_template('MantenedorProducto.html')

@app.route('/mantenedor', methods = ['POST'])

def mantenedor():
   if request.method == 'POST':
      #Insertar
      try:
         auxBotonInsertar = request.form['btoInsertar']
         if auxBotonInsertar == 'Insertar':
            auxCod = request.form['txtCod']
            auxNombre = request.form['txtNombre']
            auxValor = request.form['txtValor']
            auxStock = request.form['txtStock']
            auxProducto = claseProducto.Producto(auxCod,auxNombre, auxValor, auxStock)
            mantenedorProducto.insertar(auxProducto)
            print('Datos guardados')
            #flash('datos guardados')
      except:
         print('Datos no guardados')
      #Actualizar
      try:
         auxBotonActualizar = request.form['btoActualizar']
         if auxBotonActualizar == 'Actualizar':
            auxCod = request.form['txtCod']
            auxNombre = request.form['txtNombre']
            auxValor = request.form['txtValor']
            auxStock = request.form['txtStock']
            auxProducto = claseProducto.Producto(auxCod,auxNombre, auxValor, auxStock)
            mantenedorProducto.actualizar(auxProducto)
            print('Datos Actulizados')
            #flash('datos guardados')
      except:
         print('Datos no Actulizados')
      #Eliminar
      try:
         auxBotonEliminar = request.form['btoEliminar']
         if auxBotonEliminar == 'Eliminar':
            auxCod = request.form['txtCod']
            mantenedorProducto.eliminar(auxCod)
            print('Datos Eliminados')
            #flash('datos guardados')
      except:
         print('Datos no Eliminados')
      
      return redirect(url_for('Index'))


      

if __name__ == '__main__':
   app.run(port=3000,debug=True)
