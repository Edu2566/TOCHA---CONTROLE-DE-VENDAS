from flask import Blueprint, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
from database.dataValidation.inputValidation import *

load_dotenv()

cliente_blueprint = Blueprint('cliente', __name__, template_folder='templates')

mysql = MySQL()

@cliente_blueprint.route('/cadastro-cliente')
def cadastroCliente():
    return render_template('cadastroCliente.html')

@cliente_blueprint.route('/cadastrar-cliente', methods=['POST'])
def cadastrarCliente():
    if request.method == 'POST':
        nome = request.form['cliente-clienteform']
        endereco = request.form['endereco-clienteform']
        numero = request.form['numero_endereco-clienteform']
        cidade = request.form['cidade-clienteform']
        cep = request.form['cep-clienteform']
        estado = request.form['estado-clienteform']
        documento = request.form['documento-clienteform']
        email = request.form['email-clienteform']
        telefone = request.form['fone-clienteform']
        
        # Realizar validações antes de inserir no banco de dados
        if not is_valid_cpf_or_cnpj(documento):
            return "CPF inválido. Por favor, insira um CPF válido."

        if not is_valid_cep(cep):
            return "CEP inválido. Por favor, insira um CEP válido."

        if not is_valid_telefone(telefone):
            return "Telefone inválido. Por favor, insira um telefone válido."

        # Se todas as validações passarem, inserir no banco de dados
        conn = mysql.connection
        cursor = conn.cursor()

        try:
            sql = """
                INSERT INTO clientes (nome, endereco, numero, cidade, cep, estado, documento, email, telefone)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (nome, endereco, numero, cidade, cep, estado, documento, email, telefone))
            conn.commit()

            return redirect(url_for('cliente.cadastroCliente'))

        except Exception as e:
            conn.rollback()
            return f"Erro ao cadastrar cliente: {str(e)}"

        finally:
            cursor.close()

    return "Método GET não permitido para esta rota."

@cliente_blueprint.route('/lista-clientes')
def listaClientes():
    return render_template('listaClientes.html')