from flask import Flask, request, json
from flask_restful import Resource, Api
from skills import *
app = Flask(__name__)
api = Api(app)

tasks = [{
    'id': 0,
    'name': 'Chris',
    'task': 'Play Video Game',
    'status': 'In curse'
}, {
    'id': 1,
    'name': 'Josue',
    'task': 'Program',
    'status': 'Fail'
}]


class Begin(Resource):
    def get(self):
        return 'Hello!'


class Tasks(Resource):
    def get(self):
        return tasks

    def post(self):
        response = json.loads(request.data)
        id = len(tasks)
        response['id'] = id
        tasks.append(response)
        return tasks[id]


api.add_resource(Begin, '/')
api.add_resource(Tasks, '/tasks/')
api.add_resource(Skills, '/skills/')
api.add_resource(Skill_Index_List, '/skills/<int:id>/')


if __name__ == '__main__':
    app.run(debug=True)