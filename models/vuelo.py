from config.db import  db, ma, app

class Vuelo(db.Model):
    __tablename__ = "tblvuelo"

    id = db.Column(db.Integer, primary_key =True)
    numeroDeVuelo = db.Column(db.Integer)
    horaDeSalida = db.Column(db.DateTime)
    horaDeLlegada = db.Column(db.DateTime)
    duracion = db.Column(db.Integer)
    fecha = db.Column(db.DateTime)
    origen = db.Column(db.Integer, db.ForeignKey('tblciudad.id'))    
    nombreDeLaAereolinea = db.Column(db.Integer, db.ForeignKey('tblaerolinea.id'))
    avion = db.Column(db.Integer, db.ForeignKey('tblavion.id'))
    destino = db.Column(db.Integer, db.ForeignKey('tblciudad.id'))
    

    def __init__(self, numeroDeVuelo, horaDeSalida, horaDeLlegada, duracion, origen, nombreDeLaAereolinea, avion, fecha, destino ) :
       self.numeroDeVuelo = numeroDeVuelo
       self.horaDeSalida = horaDeSalida
       self.horaDeLlegada = horaDeLlegada
       self.duracion = duracion
       self.origen = origen
       self.fecha = fecha
       self.avion = avion
       self.nombreDeLaAereolinea= nombreDeLaAereolinea
       self.destino= destino

with app.app_context():
    db.create_all()

class VuelosSchema(ma.Schema):
    class Meta:
        fields = ('id','numeroDeVuelo', 'horaDeSalida', 'horaDeLlegada', 'duracion', 'origen', 'nombreDeLaAereolinea', 'destino', 'avion', 'fecha')