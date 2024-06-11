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

#Função de deletar dado
@produto_blueprint.route('/deletar-produto/<int:id_produto>', methods=['POST'])
def deletarProduto(id_produto):
    conn = mysql.connection
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM produtos WHERE id_produto = %s", (id_produto,))
        conn.commit()
        return redirect(url_for('produto.listaProduto'))
    except Exception as e:
        conn.rollback()
        return f"Erro ao deletar produto: {str(e)}"
    finally:
        cursor.close()

@produto_blueprint.route('/editar-produto/<int:id_produto>', methods=['GET'])
def editarProduto(id_produto):
    conn = mysql.connection
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM produtos WHERE id_produto = %s", (id_produto,))
        produto = cursor.fetchone()
        if produto:
            # Formatar o preço para exibir com vírgula
            preco_br = "{:.2f}".format(produto[2]).replace('.', ',')
            produto = list(produto)  # Convertendo o tuple para lista
            produto[2] = preco_br  # Substituindo o preço formatado
            return render_template('editarProduto.html', produto=produto)
        else:
            return "Produto não encontrado."
    except Exception as e:
        return f"Erro ao buscar produto: {str(e)}"
    finally:
        cursor.close()

@produto_blueprint.route('/atualizar-produto/<int:id_produto>', methods=['POST'])
def atualizarProduto(id_produto):
    nome = request.form['nome-produtoform']
    preco_br = request.form['preco-produtoform']
    quantidade = request.form['quantidade-produtoform']
    descricao = request.form['descricao-produtoform']

    # Convertendo o preço para o formato americano
    preco = float(preco_br.replace(',', '.'))

    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE produtos SET nome_produto = %s, preco = %s, quantidade = %s, descricao_produto = %s WHERE id_produto = %s", (nome, preco, quantidade, descricao, id_produto))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('produto.listaProduto'))
    except Exception as e:
        return f"Erro ao atualizar produto: {str(e)}"
    