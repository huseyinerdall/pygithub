from os import error
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import pprint
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / '.secret', 'r') as f:
    secret = json.loads(f.read())


headers = {'Authorization': 'token ' + secret['GITHUB_ACCESS_TOKEN']}

login = requests.get('https://api.github.com/user', headers=headers)

class GitAuth(APIView):
    def post(self,request):
        return Response(requests.get('https://api.github.com/users/huseyinerdall/repos').json(),200,content_type='application/json')

    def get(self, request):
        return Response(requests.get('https://api.github.com/users/huseyinerdall/repos').json())

    def delete(self, request):
        return Response('deleted')

class GitRepoActions(APIView):
    def __init__(self):
        self.username = 'huseyinerdall'
        self.headers = {'Authorization': 'token ' + secret['GITHUB_ACCESS_TOKEN']}
    def post(self,request):
        return Response(requests.get('https://api.github.com/users/huseyinerdall/repos').json(),200,content_type='application/json')

    def put(self,request):
        desired = request.body.decode('utf8').replace("'", '"')
        data = json.loads(desired)
        name = data['name']
        description = data['description']
        print(name,description)
        payload = {'name': name, 'description': description, 'auto_init': 'true'}
        result = requests.post('https://api.github.com/' + 'user/repos', auth=(self.username,secret['GITHUB_ACCESS_TOKEN']), data=json.dumps(payload)).json()

        return Response(result)

    def delete(self, request):
        if request.headers.get('Repo Name') == '':
            print('Error')
            return
        repo = 'hemensil'#request.headers.get('Repo Name')
        result = requests.delete('https://api.github.com/' + 'repos/' + self.username + '/' + repo, headers=headers).json()
        print(result)
        return Response(result)

    def get(self, request):
        return Response('deleted')

class APIStructure(APIView):
    def get(self, request):
        structure = {
            "/auth":"For github authentication",
            "/repos":"For list user's repositories",
            "/actions": "For repositıry actions"
        }
        return Response(structure)

    def options(self, request):
        pprint.pprint(super().options(request).name)
        return super().options(request)