from config.db import  db, ma, app

class Aeropuerto(db.Model):
    __tablename__ = "tblaeropuerto"

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    ubicacion = db.Column(db.String(50))
    numeroDePistas = db.Column(db.Integer)
    terminales = db.Column(db.Integer)
    capacidad = db.Column(db.Integer)
    

    def __init__(self, nombre,ubicacion,numeroDePistas,terminales,capacidad ) :
       self.nombre = nombre
       self.ubicacion = ubicacion
       self.numeroDePistas = numeroDePistas
       self.terminales = terminales
       self.capacidad = capacidad


with app.app_context():
    db.create_all()

class AeropuertosSchema(ma.Schema):
    class Meta:
        fields = ('id', "nombre", "ubicacion", "numeroDePistas", "terminales", "capacidad")