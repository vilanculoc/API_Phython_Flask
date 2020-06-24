from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import lista_habilidades
import json


app = Flask(__name__)
api = Api(app)


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


class Desenvolvedor(Resource):
    def get(self, id):

        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'desenvolvedor de Id {} nao existe'.format(id)
            response = {'status':'error', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhacido. Procure o Administrador da API'
            response = {'status': 'error', 'mensagem': mensagem}

        return response


    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id]= dados
        return dados

    def delete(self,id):
        desenvolvedores.pop(id)

        return {'status':'sucesso','mensagem':'registo apagado'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    # return jsonify({'status':'sucesso','mensagem':'Registro Inserido'})

api.add_resource(Desenvolvedor,'/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(lista_habilidades,'/habilidades/' )
if __name__ == '__main__':
    app.run(debug=True)