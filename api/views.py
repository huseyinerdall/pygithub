from os import error
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import pprint
import json
from pathlib import Path
import urllib.parse
from base64 import b64encode


BASE_DIR = Path(__file__).resolve().parent.parent
username = ''
token = ''


class GitAuth(APIView):
    def __init__(self) -> None:
        super().__init__()
        with open(BASE_DIR / '.secret', 'r') as f:
            self.secret = json.loads(f.read())

        self.headers = {'Authorization': 'token ' + self.secret['GITHUB_ACCESS_TOKEN']}

    def get_headers():
        with open(BASE_DIR / '.secret', 'r') as f:
            secret = json.loads(f.read())
        headers = {'Authorization': 'token ' + secret['GITHUB_ACCESS_TOKEN']}
        return headers

    def get_token():
        with open(BASE_DIR / '.secret', 'r') as f:
            secret = json.loads(f.read())
        token = secret['GITHUB_ACCESS_TOKEN']
        return token

    def get_username():
        with open(BASE_DIR / '.secret', 'r') as f:
            secret = json.loads(f.read())
        username = secret['GITHUB_USERNAME']
        return username


    def post(self,request):
        global username
        token = request.data['token']
        print(token)
        self.headers = {'Authorization': 'token ' + token}
        result = requests.get('https://api.github.com/user', headers=self.headers).json()
        print(result)
        if result['login']:
            temp = {
                "GITHUB_ACCESS_TOKEN": token
            }
            with open(BASE_DIR / '.secret', 'w') as f:
                json.dump(temp, f)
            return Response(result)

        return Response(result)

    #def get(self, request):
    #    return Response(requests.get('https://api.github.com/users/huseyinerdall/repos').json())

    def delete(self, request):
        return Response('deleted')

class GitRepoActions(APIView):
    def __init__(self):
        pass
    
    def put(self,request):
        name = request.data['reponame']
        description = request.data['description']
        """
        desired = request.body.decode('utf8').replace("'", '"')
        data = json.loads(desired)
        name = data['name']
        description = data['description']
        """
        print(name,description)
        payload = {'name': name, 'description': description, 'auto_init': 'true'}
        result = requests.post('https://api.github.com/' + 'user/repos', auth=(username,GitAuth.get_token()), data=json.dumps(payload)).json()

        return Response(result)

    def delete(self, request):
        if request.headers.get('reponame') == '':
            print('Error')
            return Response('Repo bulunamadı!')
        repo = request.headers.get('reponame')
        result = requests.delete('https://api.github.com/' + 'repos/' + username + '/' + repo, headers=self.headers).json()
        print(result)
        return Response(result)

    def get(self, request):
        return Response('deleted')

    def options(self,request,repo_name):
        print(request.headers.get('reponame'))
        content = request.data['content']
        message = request.data['message']
        sha = request.data['sha']
        path = request.data['path']
        repo_name = request.data['repo_name']
        if not isinstance(content, bytes):
            content = content.encode("utf-8")
        content = b64encode(content).decode("utf-8")

        payload = {
            "message": message,
            "content": content,
            "sha": sha
        }

        result = requests.put(f"https://api.github.com/repos/huseyinerdall/{repo_name}/contents/{urllib.parse.quote(path)}",headers=self.headers,data=json.dumps(payload)).json()
        return Response(result)

    def post(self, request):
        self.username = username
        
        with open(BASE_DIR / '.secret', 'r') as f:
            self.secret = json.loads(f.read())
        self.headers = GitAuth.get_headers()

        if request.data['_method'] == 'DELETEREPO':
            repo = request.data['reponame']
            if repo == '':
                print('Error')
                return Response('Repo bulunamadı!')
            print(GitAuth.get_headers())
            result = requests.delete('https://api.github.com/' + 'repos/' + 'huseyinerdall' + '/' + repo, headers=GitAuth.get_headers()).text
            print(result)
            return Response(result)
        elif request.data['_method'] == 'EDITFILE':
            print(self.headers,username)
            content = request.data['content']
            message = request.data['message']
            sha = request.data['sha']
            path = request.data['path']
            repo_name = request.data['repo_name']
            if not isinstance(content, bytes):
                content = content.encode("utf-8")
            content = b64encode(content).decode("utf-8")

            payload = {
                "message": message,
                "content": content,
                "sha": sha
            }
            result = requests.put(f"https://api.github.com/repos/huseyinerdall/{repo_name}/contents/{urllib.parse.quote(path)}",headers=self.headers,data=json.dumps(payload)).json()
            return Response(result)

        elif request.data['_method'] == 'DELETEFILE':
            content = request.data['content']
            message = request.data['message']
            sha = request.data['sha']
            path = request.data['path']
            repo_name = request.data['repo_name']
            if not isinstance(content, bytes):
                content = content.encode("utf-8")
            content = b64encode(content).decode("utf-8")

            payload = {
                "message": 'DELETE VIA GITHUB ENTEGRATOR',
                "sha": sha
            }
            result = requests.delete(f"https://api.github.com/repos/huseyinerdall/{repo_name}/contents/{urllib.parse.quote(path)}",headers=self.headers,data=json.dumps(payload)).json()
            return Response(result)

    def delete_file(
        self,
        path,
        message,
        sha
    ):

        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            f"{self.url}/contents/{urllib.parse.quote(path)}",
            input=url_parameters,
        )

        return {
            "commit": github.Commit.Commit(
                self._requester, headers, data["commit"], completed=True
            ),
            "content": github.GithubObject.NotSet,
        }


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


class GithubUserInfo(APIView):

    def __init__(self) -> None:
        super().__init__()

        with open(BASE_DIR / '.secret', 'r') as f:
            self.secret = json.loads(f.read())

        self.headers = {'Authorization': 'token ' + self.secret['GITHUB_ACCESS_TOKEN']}

    def post(self, request):
        username = request.data['username']
        result = requests.get(f"https://api.github.com/users/{username}",headers=self.headers).json()
        print(result)
        return Response(result)

class GitGetContents(APIView):
    def post(self, request):
        type = request.data['type']
        if type == 'file':
            url = request.data['url']
            result = requests.get(url).text
            return Response(result)
        elif type == 'json':
            url = request.data['url']
            result = requests.get(url).json()
            return Response(result)