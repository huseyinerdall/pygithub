import base64
from github import Github
from pprint import pprint
import time
import json
import requests
import os


with open('../.secret', 'r') as f:
    secret = json.loads(f.read())

print(secret)
#os.environ.setdefault('GITHUB_ACCESS_TOKEN', secret['GITHUB_ACCESS_TOKEN'])

headers = {'Authorization': 'token ' + secret['GITHUB_ACCESS_TOKEN']}



login = requests.get('https://api.github.com/user', headers=headers)
print(login.json())