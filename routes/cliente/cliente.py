from flask import Blueprint, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from database.dataValidation.inputValidation import *

cliente_blueprint = Blueprint('cliente', __name__, template_folder='templates', static_folder='static-cliente')

mysql = MySQL()

# Template e função de cadastro
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
        doctype = request.form['doctype-clienteform']
        documento = request.form['documento-clienteform']
        email = request.form['email-clienteform']
        telefone = request.form['fone-clienteform']
        
        # Realizar validações antes de inserir no banco de dados
        if not is_valid_cpf_or_cnpj(documento):
            return "CPF/CNPJ inválido. Por favor, insira um CPF/CNPJ válido."

        if not is_valid_cep(cep):
            return "CEP inválido. Por favor, insira um CEP válido."

        if not is_valid_telefone(telefone):
            return "Telefone inválido. Por favor, insira um telefone válido."

        # Se todas as validações passarem, inserir no banco de dados
        conn = mysql.connection
        cursor = conn.cursor()

        try:
            sql = """
                INSERT INTO clientes (nome, endereco, numero, cidade, cep, estado, doctype, documento, email, telefone)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (nome, endereco, numero, cidade, cep, estado, doctype, documento, email, telefone))
            conn.commit()

            return redirect(url_for('cliente.cadastroCliente'))

        except Exception as e:
            conn.rollback()
            return f"Erro ao cadastrar cliente: {str(e)}"

        finally:
            cursor.close()

    return "Método GET não permitido para esta rota."

#template e função de lista
@cliente_blueprint.route('/lista-clientes')
def listaClientes():
    conn = mysql.connection
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, nome, endereco, documento FROM clientes")
        clientes = cursor.fetchall()
    except Exception as e:
        return f"Erro ao buscar clientes: {str(e)}"
    finally:
        cursor.close()

    return render_template('listaClientes.html', clientes=clientes)

#Função de deletar dado
@cliente_blueprint.route('/deletar-cliente/<int:id>', methods=['POST'])
def deletarCliente(id):
    conn = mysql.connection
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        conn.commit()
        return redirect(url_for('cliente.listaClientes'))
    except Exception as e:
        conn.rollback()
        return f"Erro ao deletar cliente: {str(e)}"
    finally:
        cursor.close()

#Função e Template de Editar dados
@cliente_blueprint.route('/editar-cliente/<int:id>', methods=['GET'])
def editarCliente(id):
    conn = mysql.connection
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        cliente = cursor.fetchone()
        if cliente:
            return render_template('editarCliente.html', cliente=cliente)
        else:
            return "Cliente não encontrado."
    except Exception as e:
        return f"Erro ao buscar cliente: {str(e)}"
    finally:
        cursor.close()

@cliente_blueprint.route('/atualizar-cliente/<int:id>', methods=['POST'])
def atualizarCliente(id):
    if request.method == 'POST':
        nome = request.form['cliente-clienteform']
        endereco = request.form['endereco-clienteform']
        numero = request.form['numero_endereco-clienteform']
        cidade = request.form['cidade-clienteform']
        cep = request.form['cep-clienteform']
        estado = request.form['estado-clienteform']
        doctype = request.form['doctype-clienteform']
        documento = request.form['documento-clienteform']
        email = request.form['email-clienteform']
        telefone = request.form['fone-clienteform']
        
        # Realizar validações antes de atualizar no banco de dados
        if not is_valid_cpf_or_cnpj(documento):
            return "CPF/CNPJ inválido. Por favor, insira um CPF/CNPJ válido."

        if not is_valid_cep(cep):
            return "CEP inválido. Por favor, insira um CEP válido."

        if not is_valid_telefone(telefone):
            return "Telefone inválido. Por favor, insira um telefone válido."

        # Se todas as validações passarem, atualizar no banco de dados
        conn = mysql.connection
        cursor = conn.cursor()

        try:
            sql = """
                UPDATE clientes
                SET nome = %s, endereco = %s, numero = %s, cidade = %s, cep = %s, estado = %s, doctype = %s, documento = %s, email = %s, telefone = %s
                WHERE id = %s
            """
            cursor.execute(sql, (nome, endereco, numero, cidade, cep, estado, doctype, documento, email, telefone, id))
            conn.commit()

            return redirect(url_for('cliente.listaClientes'))

        except Exception as e:
            conn.rollback()
            return f"Erro ao atualizar cliente: {str(e)}"

        finally:
            cursor.close()

    return "Método GET não permitido para esta rota."



