import json
import time
import unittest

from nose.tools import assert_is_not_none, assert_list_equal
from wiremock.server.server import WireMockServer
from wiremock.constants import Config
from wiremock.client import *

from schema import TodoSchema
from service import Service


class MyTestClassBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wiremock_server = WireMockServer()
        cls.wiremock_server.start()
        Config.base_url = 'http://localhost:{}/__admin'.format(cls.wiremock_server.port)
        cls.todo_base_url = 'http://localhost:{}'.format(cls.wiremock_server.port)
        time.sleep(1.0)
        cls.expected_todos = [{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]
        mapping = Mapping(
            priority=100,
            request=MappingRequest(method=HttpMethods.GET,url='/todos'),
            response=MappingResponse(status=200,body=json.dumps(cls.expected_todos)),
            persistent=False,
        )
        Mappings.create_mapping(mapping=mapping)

    @classmethod
    def tearDownClass(cls):
        cls.wiremock_server.stop()

    def test_getting_todos(self):
        todo = Service(self.todo_base_url).get_todos()
        assert_is_not_none(todo)
        assert_list_equal(todo, self.expected_todos)
        TodoSchema().load(many=True, data=todo)


if __name__ == '__main__':
    unittest.main()

