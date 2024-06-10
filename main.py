from flask import Flask
from routes.cliente.cliente import cliente_blueprint
from routes.vendas.vendas import vendas_blueprint
from routes.produtos.produtos import produto_blueprint
from database.database import configure_db

app = Flask(__name__, static_folder='static', static_url_path='/static')

configure_db(app)

app.register_blueprint(cliente_blueprint)
app.register_blueprint(vendas_blueprint)
app.register_blueprint(produto_blueprint)

if __name__ == '__main__':
    app.run(debug=True)






