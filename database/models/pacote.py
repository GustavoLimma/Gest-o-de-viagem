from peewee import Model, CharField, DecimalField, DateTimeField
from database.database import db
import datetime


class Pacote(Model):
    nome = CharField()
    descricao = CharField()
    preco = DecimalField(max_digits=10, decimal_places=2)
    data_inicio = DateTimeField()
    data_fim = DateTimeField()
    data_criacao = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db