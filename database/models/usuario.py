from peewee import Model, CharField
from database.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db
