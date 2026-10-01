from flask import Flask, render_template, request

app = Flask(__name__)

classificacao = {
    "abaixo": 18.5,
    "normal": 25,
    "sobrepeso": 30
}

@app.route('/', methods=['POST', 'GET'])
def pagina_inicial():

    resposta = {}
    valores = {}

    erros = []

    if request.method == 'POST':
        nome = request.form.get('nome')
        peso_str = request.form.get('peso')
        altura_str = request.form.get('altura')

        peso = 0
        altura = 0

        if not nome:
            erros.append('O nome é obrigatório.')
        elif len(nome) < 3:
            erros.append('O nome deve ter pelo menos 3 caracteres.')

        if not peso_str:
            erros.append('O peso é obrigatório.')
        else:
            #replace(peso_str, ',', '.')
            peso = float(peso_str)

            if peso < 1:
                erros.append('Peso tem que ser maior que 1.')

        if not altura_str:
            erros.append('A altura é obrigatória.')
        else:
            #replace(altura_str, ',', '.')
            altura = float(altura_str)

            if altura < 0.5:
                erros.append('Altura tem que ser maior que 0.5.')

        valores = {
            "nome": nome,
            "peso": peso,
            "altura": altura
        }

        if not erros:            
            imc = (peso / (altura * altura))

            if imc <= classificacao.get('abaixo'):
                resposta = {
                    "imc": imc,
                    "descricao": "🔵 Abaixo do peso",
                    "cor": "alert-info"
                }
            elif imc <= classificacao.get('normal'):
                resposta = {
                    "imc": imc,
                    "descricao": "🟢 Peso normal",
                    "cor": "alert-success"
                }
            elif imc <= classificacao.get('sobrepeso'):
                resposta = {
                    "imc": imc,
                    "descricao": "🟡 Sobrepeso",
                    "cor": "alert-warning"
                }
            else:
                resposta = {
                    "imc": imc,
                    "descricao": "🔴 Obesidade",
                    "cor": "alert-danger"
                }

    return render_template('index.html',
                            resposta=resposta,
                            valores=valores,
                            erros=erros)

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')


if __name__ == '__main__':
    app.run(debug=True)