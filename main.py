from flask import Flask
from routes.customer.customer import customer_blueprint
from routes.vendas.vendas import vendas_blueprint
from routes.produtos.produtos import produto_blueprint
from routes.vendedores.vendedores import vendedores_blueprint
from database.database import configure_db

app = Flask(__name__, static_folder='static', static_url_path='/static')

configure_db(app)

app.register_blueprint(customer_blueprint)
app.register_blueprint(vendas_blueprint)
app.register_blueprint(produto_blueprint)
app.register_blueprint(vendedores_blueprint)

if __name__ == '__main__':
    app.run(debug=True)






