from peewee import *

db = SqliteDatabase('base.db')

class Tenis(BaseModel):
    size = CharField(length=10)
    model = CharField(length=50)
    precio = CharField(length=20)

    class Meta:
               database = db  
