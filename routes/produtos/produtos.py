from flask import Blueprint, request, render_template, redirect, url_for
from flask_mysqldb import MySQL

produto_blueprint = Blueprint('produto', __name__, template_folder='templates', static_folder='static-produto')

mysql = MySQL()

@produto_blueprint.route('/cadastro-produto', methods=['GET'])
def cadastroProduto():
    return render_template('cadastroProduto.html')

@produto_blueprint.route('/cadastrar-produto', methods=['POST'])
def cadastrarProduto():
    nome = request.form['nome-produtoform']
    preco_br = request.form['preco-produtoform']
    quantidade = request.form['quantidade-produtoform']
    descricao = request.form['descricao-produtoform']

    preco = float(preco_br.replace(',', '.'))

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO produtos (nome_produto, preco, quantidade, descricao_produto) VALUES (%s, %s, %s, %s)", (nome, preco, quantidade, descricao))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('produto.cadastroProduto'))

@produto_blueprint.route('/lista-produto')
def listaProduto():
    conn = mysql.connection
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id_produto, nome_produto, preco, quantidade, descricao_produto FROM produtos")
        produto = cursor.fetchall()
    except Exception as e:
        return f"Erro ao buscar produto: {str(e)}"
    finally:
        cursor.close()

    return render_template('listaProduto.html', produto=produto)
