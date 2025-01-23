from flask import Blueprint, render_template, request, jsonify
from database.models.pacote import Pacote

pacote_route = Blueprint('pacote', __name__)

@pacote_route.route('/')
def pacote():
    return render_template('pacote/home_pacote.html')

@pacote_route.route('/list')
def lista_pacotes():
    nome = request.args.get('nome', '').strip()
    if nome:
        pacotes = Pacote.select().where(Pacote.nome.contains(nome))
    else:
        pacotes = Pacote.select() 
    return render_template('pacote/lista_pacotes.html', pacotes=pacotes)

@pacote_route.route('/', methods=['POST'])
def inserir_pacotes():
    data = request.json

    novo_pacote = Pacote.create(
        nome = data['nome'],
        descricao = data['descricao'],
        preco = data['preco'],
        data_inicio = data['data_inicio'],
        data_fim = data['data_fim']
    )

    return render_template('pacote/item_pacote.html', pacote = novo_pacote)
 
@pacote_route.route('/new')
def form_pacotes():
    return render_template('pacote/form_pacotes.html')

@pacote_route.route('/<int:pacote_id>')
def detalhe_pacote(pacote_id):
    pacote = Pacote.get_or_none(Pacote.id == pacote_id)
    if not pacote:
        return jsonify({'error': 'Pacote não encontrado'}), 404
    return render_template('pacote/detalhe_pacotes.html', pacote=pacote)

@pacote_route.route('/<int:pacote_id>/edit')
def form_edit_pacote(pacote_id):
    pacote = Pacote.get_or_none(Pacote.id == pacote_id)
    if not pacote:
        return jsonify({'error': 'Pacote não encontrado'}), 404
    return render_template('pacote/form_pacotes.html', pacote=pacote)

@pacote_route.route('/<int:pacote_id>/update', methods=['PUT'])
def atualizar_pacote(pacote_id):
    data = request.json
    
    pacote_editado = Pacote.get_by_id(Pacote.id)
    pacote_editado.nome = data['nome']
    pacote_editado.descricao = data['descricao']
    pacote_editado.preco = data['preco']
    pacote_editado.data_inicio = data['data_inicio']
    pacote_editado.data_fim = data['data_fim']
    pacote_editado.save()

    return render_template('pacote/item_pacote.html', pacote=pacote_editado)


@pacote_route.route('/<int:pacote_id>/delete', methods=['DELETE'])
def deletar_pacote(pacote_id):
    pacote = Pacote.get_by_id(Pacote.id)
    pacote.delete_instance()
    return{'delete': 'ok'}