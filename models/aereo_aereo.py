from config.db import  db, ma, app

class Aero(db.Model):
    __tablename__ = "tblaero_aero"

    id = db.Column(db.Integer, primary_key =True)
    idaerolinea = db.Column(db.Integer, db.ForeignKey('tblaerolinea.id'))
    idaeropuerto= db.Column(db.Integer, db.ForeignKey('tblaeropuerto.id'))

    def __init__(self, idaerolinea, idaeropueto) :
        self.idaerolinea = idaerolinea
        self.idaeropuerto = idaeropueto

with app.app_context():
    db.create_all()

class AerosSchema(ma.Schema):
    class Meta:
        fields = ('id','idaeropuerto', 'idaerolinea')