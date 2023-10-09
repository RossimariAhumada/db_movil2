from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.aeropuerto import Aeropuerto, AeropuertosSchema

ruta_aeropuertos = Blueprint("ruta_aeropuerto", __name__)

aeropuerto_schema = AeropuertosSchema()
aeropuertos_schema = AeropuertosSchema(many=True)

@ruta_aeropuertos.route('/aeropuertos', methods=['GET'])
def aeropuerto():
    resultall = Aeropuerto.query.all() #Select * from Aeropuertos
    resultado_aeropuerto= aeropuertos_schema.dump(resultall)
    return jsonify(resultado_aeropuerto)

@ruta_aeropuertos.route('/saveaeropuerto', methods=['POST'])
def save():
    nombre = request.json['nombre']
    ubicacion = request.json['ubicación']
    numeroDePistas = request.json['numero de pistas']
    terminales = request.json['terminales']
    capacidad = request.json['capacidad']
    new_aeropuerto = Aeropuerto(nombre, ubicacion, numeroDePistas, terminales, capacidad)
    db.session.add(new_aeropuerto)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_aeropuertos.route('/updateaeropuerto', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    ubicacion = request.json['ubicación']
    numeroDePistas = request.json['numero de pistas']
    terminales = request.json['terminales']
    capacidad = request.json['capacidad']
    aeropuerto = Aeropuerto.query.get(id)   
    if aeropuerto :
        print(aeropuerto) 
        aeropuerto.nombre = nombre
        aeropuerto.ubicacion = ubicacion
        aeropuerto.numeroDePistas = numeroDePistas
        aeropuerto.terminales = terminales
        aeropuerto.capacidad = capacidad
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_aeropuertos.route('/deleteaeropuerto/<id>', methods=['DELETE'])
def eliminar(id):
    aeropuerto = Aeropuerto.query.get(id)
    db.session.delete(aeropuerto)
    db.session.commit()
    return jsonify(aeropuerto_schema.dump(aeropuerto))