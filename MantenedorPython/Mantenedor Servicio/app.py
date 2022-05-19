#Este es el programa de arranque
import mantenedorServicio
import claseServicio
from flask import Flask, render_template, request, flash, redirect, url_for



app = Flask(__name__)

#Se rutea el home

@app.route('/')

def Index():
   #return 'Holi'
   datos = mantenedorServicio.consultar()
   return render_template('MantenedorServicio.html',servicios=datos)
   #return render_template('MantenedorServicio.html')

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
            auxServicio = claseServicio.Servicio(auxCod,auxNombre, auxValor)
            mantenedorServicio.insertar(auxServicio)
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
            auxServicio = claseServicio.Servicio(auxCod,auxNombre,auxValor)
            mantenedorServicio.actualizar(auxServicio)
            print('Datos Actulizados')
            #flash('datos guardados')
      except:
         print('Datos no Actulizados')
      #Eliminar
      try:
         auxBotonEliminar = request.form['btoEliminar']
         if auxBotonEliminar == 'Eliminar':
            auxCod = request.form['txtCod']
            mantenedorServicio.eliminar(auxCod)
            print('Datos Eliminados')
            #flash('datos guardados')
      except:
         print('Datos no Eliminados')
      
      return redirect(url_for('Index'))


      

if __name__ == '__main__':
   app.run(port=3000,debug=True)
