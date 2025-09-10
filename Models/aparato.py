from peewee import *

db = SqliteDatabase('data.db')

class Aparato(BaseModel):
    marca = CharField(length=20)
    color = CharField(length=20)
    caracteristica = CharField(length=30)
    diseño = CharField(length=30)
    precio = CharField(length=20)

    class Meta:
           database = db
