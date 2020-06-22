from flask import Flask, jsonify, request
import json

app = Flask(__name__)


desenvolvedores = [
    { 'id':'0',
     'nome': 'Celsa',
     'habilidade': ['Phython', 'Flask']
     },
    {'id':'1',
        'nome':'Rafael',
     'habilidade':['Phython','Django']
    }
]

@app.route('/dev/<int:id>', methods=['GET','PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method=='GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'desenvolvedor de Id {} nao existe'.format(id)
            response = {'status':'error', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhacido. Procure o Administrador da API'
            response = {'status': 'error', 'mensagem': mensagem}

        return jsonify(response)

    elif request.method=='PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'registo apagado'})


#lista todos os desenvedores e regista
@app.route('/dev/', methods =['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
       # return jsonify({'status':'sucesso','mensagem':'Registro Inserido'})

    elif request.method =='GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)
