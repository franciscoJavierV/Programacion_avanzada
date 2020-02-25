## @imports
import json

from flask import Flask, render_template, request, redirect , url_for,flash
from datetime import datetime
from flaskext.mysql import MySQL

##Primeras instancias de flask y la db


app = Flask(__name__)

mysql = MySQL()
 
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'francisco'
app.config['MYSQL_DATABASE_DB'] = 'pasteleria'

app.secret_key = "mysecretkey"

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
        cedula = request.args.get('cedula')
    
        if (nombre != ''):
            cedul = int(cedula)
            cur.execute("INSERT INTO persona_externa (cedula , nombre , direccion) VALUES(\"%s\",\"%s\",\"%s\")"%(cedul,nombre,direccion))
            conn.commit()            
            return "cliente" + nombre 
        else:    
            return render_template('index.html')
    except:
        return render_template('index.html')
     
    
        
 ### ruta renderizado de pedir   
@app.route('/pedir.html', methods = ['GET'])
def pedir():
    try:
        ingredientes = []
        pastel = request.args.get('Pastel')
        nombre = request.args.get('nombre')
        porciones = request.args.get('porciones')
        cedula = request.args.get('cedula')
        descripcion = request.args.get('Descripcion')
        tipo = request.args.get('tipo')

        if (request.args.get('fresa') != ''):
            fresa = request.args.get('fresa')
            ingredientes.append(fresa)
        if (request.args.get('chocolate') != ''):
            chocolate = request.args.get('chocolate')
            ingredientes.append(chocolate)
        if (request.args.get('mani') != ''):
            mani = request.args.get('mani')
            ingredientes.append(mani)  

        if (nombre != ''):
            cur.execute("INSERT INTO pastel VALUES(\"%s\",\"%s\",\"%s\")"%(cedula,pastel,tipo))        
            conn.commit()
            orden  = {"nombre":nombre, "ceduladel cliente":cedula , "descripcion":descripcion , "tipo" : tipo ,"pastel":pastel, "porciones":porciones , "ingredientes":ingredientes }

            

            return redirect(url_for('pedir'))
        else:    
            return render_template('pedir.html')
    except:
        return render_template('pedir.html')

    
      
    

    ### ruta renderizado de clientes    
@app.route('/Mi_pedido.html' , methods =  ['get'])
def pedidos():
    return render_template("Mi_pedido.html")


@app.route('/mostrar_pasteles.html' , methods = ['GET'])
def pasteles():

    buscar = request.args.get('buscar')
    bus = int(buscar)        
    cur.execute("select * from orden where codigo_orden = '%s'" % bus) 
    data = cur.fetchall()
    return json.dumps(data)    
### listar empleados
@app.route('/lista.html')
def listar_empleados(): 
    nombre ="asa"
    cedu = 123
    pas = 1232
    pais = "col"
    experiencia = 2
    recomendador = "asada"
    tipo = "decorador"
    sal = 123
        
    cur.execute('SELECT * FROM empleado ')
    data = cur.fetchall()
    return json.dumps(data)
### LISTAS PASTELEROS
@app.route('/pasteleros.html')
def listar_pasteleros(): 
    cur.execute('SELECT * FROM empleado WHERE tipo = "pastelero"')
    data = cur.fetchall()
    return json.dumps(data)
    
### ruta renderizado de empleados    
@app.route('/empleados.html' , methods = ['GET'])
def empleados():
    try:
        nombre = request.args.get('nombre')
        cedula = request.args.get('cedula')
        salario = request.args.get('salario')
        tipo = request.args.get('tipo')
        pasaporte = request.args.get('pasaporte')
        pais = request.args.get('pais')
        experiencia = request.args.get('exp')
        recomendador = request.args.get('recomendacion')
        
        if (nombre != ''):
            sal = int(salario)
            cedul = int(cedula)
            pasap = int(pasaporte)
            exp = int(experiencia)

            cur.execute("INSERT INTO empleado VALUES(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")"%(cedul,nombre,sal,pasap,pais,exp,recomendador,tipo))        
            conn.commit()

            return "cliente" 
        else:             
            return render_template('empleados.html')
    except:
        return render_template('empleados.html')
      
        
        

    


app.run(debug=True)
