from flask import Blueprint, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from database.data_validation.input_validation import *

customer_blueprint = Blueprint('customer', __name__, template_folder='templates', static_folder='static-customer')

mysql = MySQL()

# Template and registration function
@customer_blueprint.route('/register-customer')
def register_customer():
    return render_template('register_customer.html')

@customer_blueprint.route('/insert-customer', methods=['POST'])
def insert_customer():
    if request.method == 'POST':
        name = request.form['customer-customerform']
        address = request.form['address-customerform']
        number = request.form['address_number-customerform']
        city = request.form['city-customerform']
        postal_code = request.form['postal_code-customerform']
        state = request.form['state-customerform']
        doc_type = request.form['doc_type-customerform']
        document = request.form['document-customerform']
        email = request.form['email-customerform']
        phone = request.form['phone-customerform']
        
        # Perform validations before inserting into the database
        if not is_valid_cpf_or_cnpj(document):
            return "CPF/CNPJ inválido. Por favor insira um CPF/CNPJ válido."

        if not is_valid_cep(postal_code):
            return "CEP inválido. Por favor insira um CEP válido."

        if not is_valid_telefone(phone):
            return "Número de telefone inválido. Por favor insira um número válido."

        # If all validations pass, insert into the database
        conn = mysql.connection
        cursor = conn.cursor()

        try:
            sql = """
                INSERT INTO clientes (nome, endereco, numero, cidade, cep, estado, doctype, documento, email, telefone)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (name, address, number, city, postal_code, state, doc_type, document, email, phone))
            conn.commit()

            return redirect(url_for('customer.register_customer'))

        except Exception as e:
            conn.rollback()
            return f"Erro ao registrar cliente: {str(e)}"

        finally:
            cursor.close()

    return "Método GET inválido para essa rota."

# Template and list function
@customer_blueprint.route('/list-customers')
def list_customers():
    conn = mysql.connection
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, nome, endereco, documento FROM clientes")
        customers = cursor.fetchall()
    except Exception as e:
        return f"Erro ao listar os clientes: {str(e)}"
    finally:
        cursor.close()

    return render_template('listaClientes.html', customers=customers)

# Function to delete data
@customer_blueprint.route('/delete-customer/<int:id>', methods=['POST'])
def delete_customer(id):
    conn = mysql.connection
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        conn.commit()
        return redirect(url_for('customer.list_customers'))
    except Exception as e:
        conn.rollback()
        return f"Erro ao deletar o cliente: {str(e)}"
    finally:
        cursor.close()

# Function and template to edit data
@customer_blueprint.route('/edit-customer/<int:id>', methods=['GET'])
def edit_customer(id):
    conn = mysql.connection
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        customer = cursor.fetchone()
        if customer:
            return render_template('editarCliente.html', cliente=customer)
        else:
            return "Cliente não encontrado."
    except Exception as e:
        return f"Erro ao listar os clientes: {str(e)}"
    finally:
        cursor.close()

@customer_blueprint.route('/update-customer/<int:id>', methods=['POST'])
def update_customer(id):
    if request.method == 'POST':
        name = request.form['name-customerform']
        address = request.form['address-customerform']
        number = request.form['address_number-customerform']
        city = request.form['city-customerform']
        postal_code = request.form['postal_code-customerform']
        state = request.form['state-customerform']
        doc_type = request.form['doc_type-customerform']
        document = request.form['document-customerform']
        email = request.form['email-customerform']
        phone = request.form['phone-customerform']
        
        # Perform validations before updating in the database
        if not is_valid_cpf_or_cnpj(document):
            return "CPF/CNPJ inválido. Por favor insira um CPF/CNPJ válido."

        if not is_valid_cep(postal_code):
            return "CEP inválido. Por favor insira um CEP válido."

        if not is_valid_telefone(phone):
            return "Número de telefone inválido. Por favor insira um número válido."

        # If all validations pass, update in the database
        conn = mysql.connection
        cursor = conn.cursor()

        try:
            sql = """
                UPDATE clientes
                SET nome = %s, endereco = %s, numero = %s, cidade = %s, cep = %s, estado = %s, doctype = %s, documento = %s, email = %s, telefone = %s
                WHERE id = %s
            """
            cursor.execute(sql, (name, address, number, city, postal_code, state, doc_type, document, email, phone, id))
            conn.commit()

            return redirect(url_for('customer.list_customers'))

        except Exception as e:
            conn.rollback()
            return f"Erro ao atualizar cliente: {str(e)}"

        finally:
            cursor.close()

    return "Método GET inválido para essa rota."
