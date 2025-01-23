from flask import Blueprint, render_template, request, jsonify
from database.models.reserva import Reserva
from database.models.cliente import Cliente
from database.models.pacote import Pacote

reserva_route = Blueprint('reserva', __name__)

@reserva_route.route('/')
def reserva():
    return render_template('reserva/home_reserva.html')

@reserva_route.route('/list')
def lista_reservas():
    status_list = request.args.getlist('status')
    if status_list:
        reservas = Reserva.select().where(Reserva.status.in_(status_list))
    else:
        reservas = Reserva.select() 
    return render_template('reserva/lista_reservas.html', reservas=reservas)

@reserva_route.route('/', methods=['POST'])
def inserir_reservas():
    data = request.json

    nova_reserva = Reserva.create(
        cliente = data['cliente'],
        pacote = data['pacote'],
        status = data['status'],
    )
 
    return render_template('reserva/item_reserva.html', reserva = nova_reserva)
 
@reserva_route.route('/new')
def form_reservas():
    cliente_id = request.args.get('cliente_id')
    pacote_id = request.args.get('pacote_id')

    clientes = Cliente.select()
    pacotes = Pacote.select()
    
    reserva = None

    return render_template(
        'reserva/form_reservas.html',
        clientes=clientes,
        pacotes=pacotes,
        reserva=reserva
    )

@reserva_route.route('/<int:reserva_id>')
def detalhe_reservas(reserva_id):
    reserva = Reserva.get_or_none(Reserva.id == reserva_id)
    if not reserva:
        return jsonify({'error': 'Reserva não encontrada'}), 404
    return render_template('reserva/detalhe_reservas.html', reserva=reserva)

@reserva_route.route('/<int:reserva_id>/edit')
def form_edit_reserva(reserva_id):
    try:
        reserva = Reserva.get_by_id(reserva_id)
        clientes = Cliente.select()
        pacotes = Pacote.select()
    except Reserva.DoesNotExist:
        return jsonify({'error': 'Reserva não encontrada'}), 404

    return render_template(
        'reserva/form_reservas.html',
        reserva=reserva,
        clientes=clientes,
        pacotes=pacotes
    )

@reserva_route.route('/<int:reserva_id>/update', methods=['PUT'])
def atualizar_reserva(reserva_id):
    data = request.json

    reserva_editada = Reserva.get_by_id(Reserva.id)
    reserva_editada.cliente = data['cliente']
    reserva_editada.pacote = data['pacote']
    reserva_editada.status = data['status']
    reserva_editada.save()

    return render_template('reserva/item_reserva.html', reserva=reserva_editada)


@reserva_route.route('/<int:reserva_id>/delete', methods=['DELETE'])
def deletar_reserva(reserva_id):
    reserva = Reserva.get_by_id(reserva_id)
    reserva.delete_instance()
    return {'delete': 'ok'}


