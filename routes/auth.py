from flask import Blueprint, render_template, request, redirect, url_for, session
from database.models.usuario import Usuario  # Importando o modelo User
from werkzeug.security import generate_password_hash, check_password_hash

auth_route = Blueprint('auth', __name__)

@auth_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        senha = data.get('senha')

        try:
            user = Usuario.get(Usuario.email == email)  
            if check_password_hash(user.senha, senha):
                session['usuario_id'] = user.id
                return redirect(url_for('cliente.cliente'))
            else:
                return render_template('login.html', error="Usuário ou senha inválidos")
        except Usuario.DoesNotExist:
            return render_template('login.html', error="Usuário ou senha inválidos")

    return render_template('login.html')

@auth_route.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        senha = data.get('senha')
        nome = data.get('nome')

        if Usuario.select().where(Usuario.email == email).exists():
            return render_template('register.html', error="Usuário já cadastrado")

        Usuario.create(
            nome=nome,
            email=email,
            senha=generate_password_hash(senha)
        )
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_route.route('/logout')
def logout():
    session.pop('usuario_id', None)
    return redirect(url_for('auth.login'))
