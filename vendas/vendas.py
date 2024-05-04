from flask import Blueprint, render_template

vendas_blueprint = Blueprint('vendas', __name__, template_folder='templates')

@vendas_blueprint.route('/registrar-venda')
def registrarVenda():
    return render_template('vendaExtintores.html')