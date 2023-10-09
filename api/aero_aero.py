from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.aereo_aereo import Aero, AerosSchema

ruta_aeros = Blueprint("ruta_aero", __name__)

aero_schema = AerosSchema()
aeros_schema = AerosSchema(many=True)

@ruta_aeros.route('/aeros', methods=['GET'])
def aero():
    resultall = Aero.query.all() #Select * from Aero_aeros
    resultado_aero= aeros_schema.dump(resultall)
    return jsonify(resultado_aero)

@ruta_aeros.route('/saveaero', methods=['POST'])
def save():
    idaeropuerto = request.json['idaeropuerto']
    idaerolinea = request.json['idaerolinea']
    new_aero = Aero(idaeropuerto,idaerolinea)
    db.session.add(new_aero)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_aeros.route('/updateaero', methods=['PUT'])
def Update():
    id = request.json['id']
    idaeropuerto = request.json['idaeropuerto']
    idaerolinea = request.json['idaerolinea']
    aero = Aero.query.get(id)   
    if aero :
        print(aero) 
        aero.idaeropuerto = idaeropuerto
        aero.idaerolinea = idaerolinea
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_aeros.route('/deleteaero/<id>', methods=['DELETE'])
def eliminar(id):
    aero = Aero.query.get(id)
    db.session.delete(aero)
    db.session.commit()
    return jsonify(aero_schema.dump(aero))