from peewee import Model, CharField, BooleanField, DateTimeField
from database.database import db
import datetime


class Cliente(Model):
    nome = CharField()
    cpf = CharField(unique=True)
    telefone = CharField()
    email = CharField(unique=True)
    data_criacao = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db