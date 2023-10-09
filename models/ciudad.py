from config.db import  db, ma, app

class Ciudad(db.Model):
    __tablename__ = "tblciudad"

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    pais = db.Column(db.String(50))

    def __init__(self, nombre, pais) :
       self.nombre = nombre
       self.pais = pais

with app.app_context():
    db.create_all()

class CiudadesSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'pais')