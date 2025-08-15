from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS = [{
    'id': 1,
    'titulo': 'Analista de Dados',
    'localidade': 'São Paulo, SP',
    'salario': 'R$ 3.000,00'
}, {
    'id': 2,
    'titulo': 'Engenheiro de Software',
    'localidade': 'Rio de Janeiro, RJ',
    'salario': 'R$ 4.000,00'
}, {
    'id': 3,
    'titulo': 'Desenvolvedor Web',
    'localidade': 'Belo Horizonte, MG',
    'salario': 'R$ 3.500,00'
}, {
    'id': 4,
    'titulo': 'Analista de Sistemas',
    'localidade': 'Curitiba, PR',
    'salario': 'R$ 3.200,00'
}, {
    'id': 5,
    'titulo': 'Desenvolvedor Mobile',
    'localidade': 'Porto Alegre, RS',
    'salario': 'R$ 3.800,00'
}]


@app.route('/')
def hello():
  return render_template("home.html", vagas=VAGAS)


@app.route('/vagas')
def lista_vagas():
  return jsonify(VAGAS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
