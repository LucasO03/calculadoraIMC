from flask import Flask

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return '<h1>Olá, mundo!</h1><p>Meu primeiro servidor Flask está funcionando.</p>'


# Bloco de execução: só roda quando o arquivo é executado diretamente
if __name__ == '__main__':
    app.run(debug=True)