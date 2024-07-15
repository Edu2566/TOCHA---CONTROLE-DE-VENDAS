from flask import Blueprint, render_template

vendas_blueprint = Blueprint('vendas', __name__, template_folder='templates', static_folder='static-vendas')

@vendas_blueprint.route('/')
def listarVenda():
    return render_template('listarVenda.html')

@vendas_blueprint.route('/registrar-venda')
def registrarVenda():
    return render_template('registrarVenda.html')