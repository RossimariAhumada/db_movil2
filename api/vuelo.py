from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vuelo import Vuelo, VuelosSchema

ruta_vuelos = Blueprint("ruta_vuelo", __name__)

vuelo_schema = VuelosSchema()
vuelos_schema = VuelosSchema(many=True)

@ruta_vuelos.route('/vuelos', methods=['GET'])
def vuelo():
    resultall = Vuelo.query.all() #Select * from Vuelos
    resultado_vuelo= vuelos_schema.dump(resultall)
    return jsonify(resultado_vuelo)

@ruta_vuelos.route('/savevuelo', methods=['POST'])
def save():
    numeroDeVuelo = request.json['numero de vuelo']
    horaDeSalida = request.json['hora de salida']
    horaDeLlegada = request.json['hora de llegada']
    duracion = request.json['duracion']
    fecha = request.json['fecha']
    origen = request.json['origen']
    nombreDeLaAereolinea = request.json['Nombre de la aerolinea']
    avion = request.json['avion']
    destino = request.json['destino']
    new_vuelo = Vuelo(numeroDeVuelo, horaDeSalida, horaDeLlegada, duracion, fecha, origen, nombreDeLaAereolinea, avion, destino)
    db.session.add(new_vuelo)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_vuelos.route('/updatevuelo', methods=['PUT'])
def Update():
    id = request.json['id']
    numeroDeVuelo = request.json['numero de vuelo']
    horaDeSalida = request.json['hora de salida']
    horaDeLlegada = request.json['hora de llegada']
    duracion = request.json['duracion']
    fecha = request.json['fecha']
    origen = request.json['origen']
    nombreDeLaAereolinea = request.json['Nombre de la aerolinea']
    avion = request.json['avion']
    destino = request.json['destino']

    vuelo = Vuelo.query.get(id)   
    if vuelo :
        print(vuelo) 
        vuelo.numeroDeVuelo = numeroDeVuelo
        vuelo.horaDeSalida = horaDeSalida
        vuelo.horaDeLlegada = horaDeLlegada
        vuelo.destino = destino
        vuelo.fecha = fecha
        vuelo.origen = origen
        vuelo.nombreDeLaAerolinea = nombreDeLaAereolinea
        vuelo.avion = avion
        vuelo.destino= destino
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_vuelos.route('/deletevuelo/<id>', methods=['GET'])
def eliminar(id):
    vuelo = Vuelo.query.get(id)
    db.session.delete(vuelo)
    db.session.commit()
    return jsonify(vuelo_schema.dump(vuelo))