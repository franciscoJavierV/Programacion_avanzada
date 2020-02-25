## @imports
import json

from flask import Flask, render_template, request
from datetime import datetime
from flaskext.mysql import MySQL

##Primeras instancias de flask y la db


app = Flask(__name__)

mysql = MySQL()
 
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'francisco'
app.config['MYSQL_DATABASE_DB'] = 'pasteleria'

mysql.init_app(app)
conn = mysql.connect()
cur = conn.cursor()

app = Flask(__name__, template_folder="../Front", static_folder="../Front")

###ruta renderizado de index
@app.route('/index.html', methods=['GET'] )
def index(): 
    try:
        nombre = request.args.get('nombre')
        direccion = request.args.get('direccion')
        telefono = request.args.get('telefono')
        cedula = request.args.get('id/nit')
        tipo = request.args.get('tipo')
       
        cur.execute("INSERT INTO persona_externa VALUES(\"%s\",\"%s\",\"%s\,\"%s\")"%(cedula,nombre,direccion,fecha))        
        conn.commit()
    
        if (nombre != ''):           
            return render_template('index.html')
        else:
            return render_template('index.html')
    except:
        return render_template('index.html')
        
 ### ruta renderizado de pedir   
@app.route('/pedir.html', methods = ['GET'])
def pedir():
    ingredientes = []
    try:
        Cliente = request.args.get('Cliente')
        Pastel = request.args.get('Pastel')
        Fecha = request.args.get('Fecha')
        Descripcion = request.args.get('Descripcion')
        tipo = request.args.get('tipo')
        porciones = request.args.get('porciones')

        if (request.args.get('fresa') != ''):
            fresa = request.args.get('fresa')
            ingredientes.append(fresa)
        if (request.args.get('chocolate') != ''):
            chocolate = request.args.get('chocolate')
            ingredientes.append(chocolate)
        if (request.args.get('mani') != ''):
            mani = request.args.get('mani')
            ingredientes.append(mani)
              
        if (Cliente != ''):
            return "cliente" + Cliente + "pastel" + Pastel + "fecha" + Fecha + "descp" + Descripcion + "tipo" + tipo + "porciones" + porciones 
        else:
            return render_template('pedir.html')
    except:
        return render_template('pedir.html')
    

    ### ruta renderizado de clientes    
@app.route('/Mi_pedido.html')
def pedidos():
    return render_template("Mi_pedido.html")


@app.route('/mostrar_pasteles.html' , methods = ['GET'])
def pasteles():
    buscar = request.args.get('buscar')        
    print(buscar)
    return render_template("mostrar_pasteles.html")    
### listar empleados
@app.route('/lista.html')
def listar_empleados():    

    cur.execute('SELECT nombre FROM persona_externa ')
    data = cur.fetchall()
    return json.dumps(data)
### ruta renderizado de empleados    
@app.route('/empleados.html' , methods = ['GET'])
def empleados():
    try:
        nombre = request.args.get('nombre')
        cedula = request.args.get('cedula')
        salario = request.args.get('salario')
              
        if (nombre != ''):            
            cur.execute("INSERT INTO empleado VALUES(\"%s\",\"%s\",\"%s\")"%(cedula,nombre,salario))        
            conn.commit()    
            return "cliente" + nombre 
        else:    
            return render_template('empleados.html')
    except:
        return render_template('empleados.html')
      
        
        

    


app.run(debug=True)
