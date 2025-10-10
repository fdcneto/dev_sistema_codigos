from flask import Flask
# importando a Class Flask do modulo flask

# criar uma instancia do Flask = objeto
app = Flask(__name__)
#__name__ é o nome do modulo atual -> navegação

# Definir Rotas (Endpoints)
# quando acessar o servidor, chame essa função
@app.route('/')
def home():
    return 'Welcome to the mundo das APIs'

@app.route('/sobre')
def sobre():
    return 'Estamos na aula de DEV de Sistemas. Estamos aprendendo API com Flask'

@app.route('/contato')
def contato():
    return '21 4002-8922\n' \
    'email: ta_dificil@dev_sistemas.senai.br'

@app.route('/usuario/<nome>')
def ususario(nome):
    return f'Prezado,{nome}', 'espero que essa mensagem o encontre bem'

# Rota com parametro numérico
@app.route('/produto/<int:id>')

def produto (id):
    return f' Você escolheu o produro com {id}'

# o flask converte string em uma resposta HTTP

# EXECUTAR O SERVIDOR
if __name__ == '__main__':
    app.run(debug=True)
    # debug -> servidor no modo de desenvolvimento
    # ativa o reload automático e mostra
    # os erros de forma detalhada

