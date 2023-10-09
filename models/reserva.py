from config.db import  db, ma, app

class Reserva(db.Model):
    __tablename__ = "tblreserva"

    id = db.Column(db.Integer, primary_key =True)
    idcliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    idvuelo = db.Column(db.Integer, db.ForeignKey('tblvuelo.id'))

    def __init__(self, idcliente, idvuelo) :
       self.idcliente = idcliente
       self.idvuelo = idvuelo

with app.app_context():
    db.create_all()

class ReservasSchema(ma.Schema):
    class Meta:
        fields = ('id','idcliente')