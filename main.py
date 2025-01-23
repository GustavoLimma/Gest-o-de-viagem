from flask import Flask
from configuration import configure_all

# inicializacao
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

configure_all(app)
# execucao
app.run(debug=True)