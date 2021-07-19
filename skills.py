from flask import request, json
from flask_restful import Resource

skills = ['Java', 'C', 'Python']

class Skills(Resource):
    def get(self):
        return skills

    def post(self):
        response = json.loads(request.data)
        if response in skills:
            message = 'This Skill Already Exist'
            return {'status': 'error', 'message': message}
        else:
            skills.append(response)
            message = 'One Skill Has Been Added'
            return {'status': 'success', 'message': message}


class Skill_Index_List(Resource):
    def get(self, id):
        try:
            response = skills[id]
        except IndexError:
            message = 'Index Out Of Range'
            response = {'status': 'Error', 'message': message}
        except Exception:
            message = 'Unknown Error'
            response = {'status': 'Error', 'message': message}
        return response

    def put(self, id):
        response = json.loads(request.data)
        if response in skills:
            message = 'Skill Already Exists In The List'
            return {'status': 'Error', 'message': message}
        else:
            skills[id] = response
            return skills[id]

    def delete(self, id):
        skills.pop(id)
        return {'status': 'Success', 'message': 'Object Has Been Deleted'}
