
import mysql.connector as mc



conexao = mc.connect(host='localhost', user='root', password='admin', database='bd_agendamento')

class Banco:

    def cliente(self,nome, cpf, email, telefone, senha):
        if conexao.is_connected:
            manipulador = conexao.cursor()
            insert_sql = 'insert into clientes(nome_cliente, cpf, email, telefone, senha) values(%s,%s,%s,%s,%s)'
            valores = (nome, cpf, email, telefone, senha)
            manipulador.execute(insert_sql, valores)
            conexao.commit()
            return 'salvo com sucesso'


    def login_cliente(self, logCliente, senhaCliente):
        if conexao.is_connected:
            manipulador = conexao.cursor()
            consulta_log = 'select nome_cliente, senha from clientes where nome_cliente = %s and senha = %s '
            valores = (logCliente, senhaCliente)
            manipulador.execute(consulta_log, valores)
            dados = manipulador.fetchall()
            return len(dados)

    def dado_usuario_endereco(self, cep, rua, numero, bairro, cidade, estado):
        if conexao.is_connected:
            manipulador = conexao.cursor()
            insert_sql = 'insert into endereco(cep, rua, numero, bairro, cidade, estado) values(%s,%s,%s,%s,%s,%s)'
            valores = (cep, rua, numero, bairro, cidade, estado)
            manipulador.execute(insert_sql, valores)
            conexao.commit()
            return 'salvo com sucesso'
    


