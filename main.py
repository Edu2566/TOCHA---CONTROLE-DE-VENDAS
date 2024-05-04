from flask import Flask, render_template
from cliente.cliente import cliente_blueprint
from vendas.vendas import vendas_blueprint

app = Flask(__name__)

app.register_blueprint(cliente_blueprint)

app.register_blueprint(vendas_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)