from config.db import  db, ma, app

class Aerolinea(db.Model):
    __tablename__ = "tblaerolinea"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    numeroDeSerie = db.Column(db.Integer)
    capacidadDePasajero = db.Column(db.Integer)

    def __init__(self, nombre,numeroDeSerie,capacidadDePasajero) :
       self.nombre = nombre
       self.numeroDeSerie = numeroDeSerie
       self.capacidadDePasajero = capacidadDePasajero


with app.app_context():
    db.create_all()

class AerolineasSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','numeroDeSerie', 'capacidadDePasajero')