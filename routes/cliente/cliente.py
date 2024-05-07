from flask import Blueprint, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()

cliente_blueprint = Blueprint('cliente', __name__, template_folder='templates')

mysql = MySQL()

@cliente_blueprint.route('/cadastro-cliente')
def cadastroCliente():
    return render_template('cadastroCliente.html')

@cliente_blueprint.route('/cadastrar-cliente', methods=['POST'])
def cadastrarCliente():
    if request.method == 'POST':
        data_value = request.form['date-clienteform']
        nome = request.form['cliente-clienteform']
        endereco = request.form['endereco-clienteform']
        numero = request.form['numero_endereco-clienteform']
        cidade = request.form['cidade-clienteform']
        cep = request.form['cep-clienteform']
        estado = request.form['estado-clienteform']
        email = request.form['email-clienteform']
        telefone = request.form['fone-clienteform']

        conn = mysql.connection
        cursor = conn.cursor()

        try:
            sql = """
                INSERT INTO clientes (data, nome, endereco, numero, cidade, cep, estado, email, telefone)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (data_value, nome, endereco, numero, cidade, cep, estado, email, telefone))
            conn.commit()

            return redirect(url_for('cliente.cadastroCliente'))

        except Exception as e:
            conn.rollback()
            return f"Erro ao cadastrar cliente: {str(e)}"

        finally:
            cursor.close()

    return "Método GET não permitido para esta rota."
