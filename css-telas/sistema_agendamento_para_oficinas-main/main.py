
from flask import Flask, render_template, request, url_for, redirect
from baseDados import Banco
#from api_cep import consultaCep

app = Flask(__name__)


banc_dados = Banco()

@app.route('/')
def abre_te():
    return render_template('index.html')

@app.route('/cadastro')
def abre_cadastra():
    return render_template('cadastro.html')

@app.route('/login')
def abre_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def logar():
    nome = request.form['nomeLogin']
    senha = request.form['senhaLogin']
    resultado_login = banc_dados.login_cliente(nome, senha)
    if resultado_login == 0:
        return redirect(url_for('abre_te'))
    else:
        return render_template('index.html', msg = 'Logado com sucesso!!')

@app.route('/cadastro', methods=['POST','GET'])
def cadastra():
    nome_c = request.form['nomeCliente']
    cpf_c = request.form['cpfCliente']
    email_c = request.form['emailCliente']
    telefone_c = request.form['telefoneCliente']
    senha_c = request.form['senhaCliente']
    banc_dados.cliente(nome_c,cpf_c,email_c,telefone_c,senha_c)
    #dadosUsuarioEnd = Banco.dado_usuario_endereco(cep,rua_c,numero_c,bairro_c,cidade_c,estado_c)
    return render_template('index.html', mensagem = 'cadastrado')
    # usu = dadosUsuario, ender = dadosUsuarioEnd)



app.run(debug=True)