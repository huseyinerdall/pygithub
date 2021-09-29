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


def update_file(
        self,
        path,
        message,
        content,
        sha
    ):
        """This method updates a file in a repository

        :calls: `PUT /repos/{owner}/{repo}/contents/{path} <https://docs.github.com/en/rest/reference/repos#create-or-update-file-contents>`_
        :param path: string, Required. The content path.
        :param message: string, Required. The commit message.
        :param content: string, Required. The updated file content, either base64 encoded, or ready to be encoded.
        :param sha: string, Required. The blob SHA of the file being replaced.
        :param branch: string. The branch name. Default: the repository’s default branch (usually master)
        :param committer: InputGitAuthor, (optional), if no information is given the authenticated user's information will be used. You must specify both a name and email.
        :param author: InputGitAuthor, (optional), if omitted this will be filled in with committer information. If passed, you must specify both a name and email.
        :rtype: {
            'content': :class:`ContentFile <github.ContentFile.ContentFile>`:,
            'commit': :class:`Commit <github.Commit.Commit>`}
        """

        if not isinstance(content, bytes):
            content = content.encode("utf-8")
        content = b64encode(content).decode("utf-8")

        put_parameters = {"message": message, "content": content, "sha": sha}


        """headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            f"/repos/huseyinerdall/hibi/contents/{urllib.parse.quote(path)}",
            input=put_parameters,
        )"""
        requests.put(f"https://api.github.com/repos/huseyinerdall/hibi/contents/{urllib.parse.quote(path)}",headers=headers,data=put_parameters)


login = requests.get('https://api.github.com/user', headers=headers)
print(login.json())