from flask import Blueprint, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

vendedores_blueprint = Blueprint('vendedores', __name__, template_folder='templates', static_folder='static-vendedores')

mysql = MySQL()

@vendedores_blueprint.route('/cadastro-vendedor')
def cadastroVendedores():
    return render_template('cadastroVendedores.html')

@vendedores_blueprint.route('/cadastrar-vendedor', methods=['POST'])
def cadastrarVendedores():
    if request.method == 'POST':
        nome = request.form['vendedor-vendedorform']

        conn = mysql.connection
        cursor = conn.cursor()

        try:
            sql = """
                INSERT INTO vendedores (nome_vendedor)
                VALUES (%s)
            """
            cursor.execute(sql, (nome))
            conn.commmit()

            return redirect(url_for('vendedores.cadastroVendedores'))
    
        except Exception as e:
            conn.rollback()
            return f"Erro ao cadastrar cliente: {str(e)}"

        finally:
            cursor.close()

    return "Método GET não permitido para esta rota."

@vendedores_blueprint.route('/listar-vendendores')
def listarVendedores():
    return render_template('listarVendedores.html')