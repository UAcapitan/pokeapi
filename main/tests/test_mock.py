from unittest import TestCase, mock

from requests import Response

class MyTest(TestCase):
    def test_something(self):
        with mock.patch('main.views.get_pokemon') as mock_fetch:

            fake_response = Response(body="Some expected data body", status=200)

            mock_fetch.return_value = fake_response

            self.assertTrue(True)