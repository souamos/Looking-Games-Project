import mysql.connector, Jogo_Model
from mysql.connector import Error


def db_conect():
    con = mysql.connector.connect(host='localhost', database='new_schema', user='root', password='1234')

    if con.is_connected():
        # Buscar informação sobre o BD
        db_info = con.get_server_info()
        print('Conectado com servidor MySQL versão ' + db_info)
        # Criar um curos para executar um comando SQL
        cursor = con.cursor()
        # O comando SQL utilizado foi o select database();
        cursor.execute('select database();')
        linha = cursor.fetchone()
        print('Conectado ao banco ' + str(linha))

    if con.is_connected():
        cursor.close()
        con.close()
        print('A conexão com o BD foi encerrada.')


def db_select(jogo):
    jogoquery = Jogo_Model.Jogo(jogo.id, jogo.nome, jogo.data_lancamento, jogo.genero, jogo.sobre)
    try:
        con = mysql.connector.connect(host='localhost', database='new_schema', user='root', password='1234')

        if con.is_connected():
            cursor = con.cursor()
            cursor.execute("select * from teste where nome = '" + jogo.nome + "';")
            jogoquery = cursor.fetchone()

        return jogoquery

    except Error as e:
        print('Erro ao acessar tabela MySQL', e)

    finally:
        if con.is_connected():
            cursor.close()
            con.close()
            print('A conexão com o BD foi encerrada. \n Mostrando resultado da Consulta.')

