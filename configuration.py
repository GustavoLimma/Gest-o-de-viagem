from routes.home import home_route
from routes.cliente import cliente_route
from routes.auth import auth_route
from routes.pacotes import pacote_route
from routes.reserva import reserva_route
from database.database import db
from database.models.cliente import Cliente
from database.models.pacote import Pacote
from database.models.reserva import Reserva
from database.models.usuario import Usuario

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix='/clientes')
    app.register_blueprint(pacote_route, url_prefix='/pacotes')
    app.register_blueprint(reserva_route, url_prefix='/reservas')
    app.register_blueprint(auth_route, url_prefix='/auth')

def configure_db():
    db.connect()
    db.create_tables([Usuario])
    db.create_tables([Cliente])
    db.create_tables([Pacote])
    db.create_tables([Reserva])