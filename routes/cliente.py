from flask import Blueprint, render_template, request, jsonify
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def cliente():
    return render_template('cliente/home_cliente.html')

@cliente_route.route('/list')
def lista_clientes():
    nome = request.args.get('nome', '').strip()
    if nome:
        clientes = Cliente.select().where(Cliente.nome.contains(nome))
    else:
        clientes = Cliente.select()  # Se nenhum nome for fornecido, retorna todos os clientes

    return render_template('cliente/lista_clientes.html', clientes=clientes)

@cliente_route.route('/', methods=['POST'])
def inserir_clientes():
    data = request.json

    novo_usuario = Cliente.create(
        nome = data['nome'],
        cpf = data['cpf'],
        telefone = data['telefone'],
        email = data['email'],
    )

    return render_template('cliente/item_cliente.html', cliente = novo_usuario)
 
@cliente_route.route('/new')
def form_clientes():
    return render_template('cliente/form_clientes.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_clientes(cliente_id):
    cliente = Cliente.get_or_none(Cliente.id == cliente_id)
    if not cliente:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    return render_template('cliente/detalhe_clientes.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    cliente = Cliente.get_or_none(Cliente.id == cliente_id)
    if not cliente:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    return render_template('cliente/form_clientes.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    data = request.json

    cliente_editado = Cliente.get_by_id(Cliente.id)
    cliente_editado.nome = data['nome']
    cliente_editado.cpf = data['cpf']
    cliente_editado.telefone = data['telefone']
    cliente_editado.email = data['email']
    cliente_editado.save()
        
    return render_template('cliente/item_cliente.html', cliente=cliente_editado)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    cliente = Cliente.get_by_id(Cliente.id)
    cliente.delete_instance()
    return{'delete': 'ok'}


