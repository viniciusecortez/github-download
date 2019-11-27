import requests
from django.db import models


# Create your models here.
class ConsumeGithub:
    def __init__(self, user, repository, path):
        self.user = user
        self.repository = repository
        self.path = path

    def __consume__(self):
        response = requests.get(f'https://api.github.com/repos/{self.user}/{self.repository}/contents/{self.path}')
        return response.json()['download_url']

    @property
    def download_link(self):
        return self.__consume__()
