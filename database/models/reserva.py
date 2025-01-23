from peewee import Model, ForeignKeyField, DateTimeField, DecimalField, CharField, IntegerField
from database.database import db
import datetime
from database.models.pacote import Pacote
from database.models.cliente import Cliente


class Reserva(Model):
    cliente = ForeignKeyField(Cliente, backref='reservas', on_delete='CASCADE')
    pacote = ForeignKeyField(Pacote, backref='reservas', on_delete='CASCADE')
    data_reserva = DateTimeField(default=datetime.datetime.now)
    status = CharField()

    class Meta:
        database = db
