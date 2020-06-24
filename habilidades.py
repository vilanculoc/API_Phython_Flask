from flask_restful import Resource

habilidades = ['phython', 'flask','ruby','java']

class lista_habilidades(Resource):
    def get(self):
        return habilidades