from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.avion import Avion, AvionesSchema

ruta_aviones = Blueprint("ruta_avion", __name__)

avion_schema = AvionesSchema()
aviones_schema = AvionesSchema(many=True)

@ruta_aviones.route('/aviones', methods=['GET'])
def avion():
    resultall = Avion.query.all() #Select * from Aviones
    resultado_avion= aviones_schema.dump(resultall)
    return jsonify(resultado_avion)

@ruta_aviones.route('/saveavion', methods=['POST'])
def save():
    capacidad = request.json['capacidad']
    idaerolinea = request.json['idaerolinea']
    new_avion = Avion(capacidad, idaerolinea)
    db.session.add(new_avion)
    db.session.commit()    
    return "datos guardado con exito"

@ruta_aviones.route('/updateavion', methods=['PUT'])
def Update():
    id = request.json['id']
    capacidad = request.json['capacidad']
    idaerolinea = request.json['idaerolinea']
    numeroDeSerie = request.json['numero']
    capacidadDePasajero = request.json['Capacidad de pasajero']
    avion = Avion.query.get(id)   
    if avion :
        print(avion) 
        avion.capacidad = capacidad
        avion.idaerolinea = idaerolinea
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_aviones.route('/deleteavion/<id>', methods=['GET'])
def eliminar(id):
    avion = Avion.query.get(id)
    db.session.delete(avion)
    db.session.commit()
    return jsonify(avion_schema.dump(avion))