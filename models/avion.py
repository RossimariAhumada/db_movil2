from config.db import  db, ma, app

class Avion(db.Model):
    __tablename__ = "tblavion"

    id = db.Column(db.Integer, primary_key =True)
    modelo = db.Column(db.String(50))
    idaerolinea = db.Column(db.Integer, db.ForeignKey('tblaerolinea.id'))

    def __init__(self, nombreaerolineas,idaerolinea) :
       self.nombreaerolineas = nombreaerolineas
       self.idaerolinea = idaerolinea

with app.app_context():
    db.create_all()

class AvionesSchema(ma.Schema):
    class Meta:
        fields = ('id','nombreaerolineas', 'idaerolinea')