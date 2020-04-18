from urllib.parse import urljoin
import requests
from constants import BASE_URL


class Service:

    def __init__(self, base_url=BASE_URL):
        self.todos_url = urljoin(base_url, 'todos')

    def get_todos(self):
        response = requests.get(self.todos_url)
        if response.ok:
            return response.json()
        else:
            return None

