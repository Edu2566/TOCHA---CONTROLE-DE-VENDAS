from flask import Blueprint, render_template

cliente_blueprint = Blueprint('cliente', __name__, template_folder='templates')

@cliente_blueprint.route('/cadastro-cliente')
def cadastroCliente():
    return render_template('cadastroCliente.html')