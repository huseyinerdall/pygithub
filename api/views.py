from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import pprint

class GitAuth(APIView):
    def post(self,request):
        return Response(requests.get('https://api.github.com/users/huseyinerdall/repos').json(),200,content_type='application/json')

    def get(self, request):
        return Response(requests.get('https://api.github.com/users/huseyinerdall/repos').json())

    def delete(self, request):
        return Response('deleted')

class APIStructure(APIView):
    def get(self, request):
        structure = {
            "/auth":"For github authentication",
            "/repos":"For list user's repositories and repositıry actions"
        }
        return Response(structure)

    def options(self, request):
        pprint.pprint(super().options(request).name)
        return super().options(request)