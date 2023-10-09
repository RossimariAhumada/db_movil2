from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.cliente import Cliente, ruta_clientes
from api.reserva import Reserva, ruta_reservas
from api.aerolinea import Aerolinea, ruta_aerolineas
from api.avion import Avion, ruta_aviones
from api.ciudad import Ciudad, ruta_ciudades
from api.vuelo import Vuelo, ruta_vuelos
from api.aeropuerto import Aeropuerto, ruta_aeropuertos
from api.aero_aero import Aero, ruta_aeros


app.register_blueprint(ruta_clientes,url_prefix = '/api')
app.register_blueprint(ruta_reservas, url_prefix = '/api')
app.register_blueprint(ruta_aerolineas, url_prefix = '/api')
app.register_blueprint(ruta_aviones, url_prefix = '/api')
app.register_blueprint(ruta_ciudades, url_prefix = '/api')
app.register_blueprint(ruta_vuelos, url_prefix = '/api')
app.register_blueprint(ruta_aeropuertos, url_prefix = '/api')
app.register_blueprint(ruta_aeros, url_prefix = '/api')

# primera consulta 
@app.route('/dostablas', methods=['GET'])
def dostabla():
    datos = {}
    resultado = db.session.query(Cliente, Reserva). \
        select_from(Cliente).join(Reserva).all()
    i=0
    for clientes, reservas in resultado:
        i+=1
        datos[i]={
            'cliente':clientes.nombre,
            'reserva': reservas.id
        }
    return datos

# segunda consulta
@app.route('/consultaravion', methods=['GET'])
def consultaravion():
    datos = {}
    resultado = db.session.query( Avion, Ciudad, Aeropuerto, Aerolinea, Aero, Vuelo). \
        select_from(Avion).join(Vuelo).all()
    
    i=0
    for aviones, ciudades, aeropuertos, aerolineas, aeros, vuelos in resultado:
        i+=1
        datos[i]={
            'modelo_avion': aviones.modelo,
            'nombre_ciudad': ciudades.nombre,
            'nombre_aeropuerto': aeropuertos.nombre,
            'nombre_aerolinea':aerolineas.nombre,
            'numero_vuelo': vuelos.numeroDeVuelo
        }
    return datos

# tercera consulta
@app.route('/consultareserva', methods=['GET'])
def consultareserva():
    datos = {}
    resultado = db.session.query( Reserva, Avion, Ciudad, Aeropuerto, Aerolinea, Aero, Vuelo). \
        select_from(Vuelo).join(Reserva).all()
    
    i=0
    for reservas, aviones, ciudades, aeropuertos, aerolineas, aeros, vuelos in resultado:
        i+=1
        datos[i]={
            'id_reserva': reservas.id,
            'id_avion': aviones.id,
            'modelo_avion': aviones.modelo,
            'horaDeSalida_vuelo': vuelos.horaDeSalida,
            'horaDeLlegada_vuelo': vuelos.horaDeLlegada,
            'nombre_ciudad': ciudades.nombre,
            'nombre_aeropuerto': aeropuertos.nombre,
            'nombre_aerolinea':aerolineas.nombre,
            'numero_vuelo': vuelos.numeroDeVuelo,
            'fecha_vuelo': vuelos.fecha,
            'origen_vuelo': vuelos.origen,
            'destino_vuelo': vuelos.destino,

        }
    return datos

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')