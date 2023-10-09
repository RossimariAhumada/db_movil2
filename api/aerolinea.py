from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.aerolineas import Aerolinea, AerolineasSchema

ruta_aerolineas = Blueprint("ruta_aerolineas", __name__)

aerolinea_schema = AerolineasSchema()
aerolineas_schema = AerolineasSchema(many=True)

@ruta_aerolineas.route('/aerolineas', methods=['GET'])
def aerolinea():
    resultall = Aerolinea.query.all() #Select * from Aerolineas
    resultado_aerolinea= aerolineas_schema.dump(resultall)
    return jsonify(resultado_aerolinea)

@ruta_aerolineas.route('/saveaerolineas', methods=['POST'])
def save():
    nombre = request.json['nombre']
    numeroDeSerie = request.json['numero de serie']
    capacidadDePasajero = request.json['capacidad de pasajero']
    new_aerolinea = Aerolinea(nombre)
    db.session.add(new_aerolinea)
    db.session.commit()    
    return "datos guardado con exito"

@ruta_aerolineas.route('/updateaerolineas', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    numeroDeSerie = request.json['numero de serie']
    capacidadDePasajero = request.json['Capacidad de pasajero']
    aerolinea = Aerolinea.query.get(id)   
    if aerolinea :
        print(aerolinea) 
        aerolinea.nombre = nombre
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_aerolineas.route('/deleteaerolineas/<id>', methods=['GET'])
def eliminar(id):
    aerolinea = Aerolinea.query.get(id)
    db.session.delete(aerolinea)
    db.session.commit()
    return jsonify(aerolinea_schema.dump(aerolinea))