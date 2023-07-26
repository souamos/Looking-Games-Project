import Jogo_Model, Jogo_Controller
from flask import Flask, render_template, request

app = Flask(__name__)


# Página Inicial
@app.route('/')
def home():
    return render_template('indiano.html')


# Página retornada após inserir os dados no banco

@app.route('/insert')
def insertrender():
    return render_template('insert.html')


# Página que retorna os dados da busca
@app.route('/', methods=['POST'])
def getvalue():
    nomebox = request.form['nomedojogo']
    jogoquery = Jogo_Model.Jogo(0, str(nomebox), 0, '', '')
    jogo = Jogo_Controller.jogo_select(jogoquery)
    return render_template('pass.html', nome=jogo[1], data_lancamento=str(jogo[2]), genero=jogo[3], sobre=jogo[4])


# Página retornada após inserir os dados no banco
@app.route('/insert', methods=['GET', 'POST'])
def insertvalue():
    jogoinsert = Jogo_Model.Jogo(0, '', 0, '', '')
    jogoinsert.id = request.form['id']
    jogoinsert.nome = request.form['newgame']
    jogoinsert.data_lancamento = request.form['data_lancamento']
    jogoinsert.genero = request.form['genero']
    jogoinsert.sobre = request.form['sobre']
    return render_template('insertpass.html')


if __name__ == '__main__':
    app.run(debug=True)

