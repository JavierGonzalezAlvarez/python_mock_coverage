import unittest
from unittest import mock
from unittest.mock import patch
from names import ( 
    get_sql, get_client
)

@unittest.mock.patch(
    "builtins.print",
    autospec=True,
)
@unittest.mock.patch(
    "names.get_client",
    autospec=True,
)
class APITest(unittest.TestCase):
    '''unittest names.py'''
    def test_get_sql(self, get_client, print):
        '''test get_sql function'''
        test_cases = (
            (
                "sql_mongo",    
                {
                    "_id": "6484b7b2971c1712a7c22ee9",
                    "code": "C001",
                    "name": {
                        "name": "peter",
                        "first": "smith",
                        "last": ""
                    },
                    "role": [
                        "user"
                    ],
                    "address": [
                        {
                            "address": "pasopso",
                            "number": "12",
                            "postal_code": mock.ANY,
                            "province": mock.ANY,
                            "state": mock.ANY,
                            "status": mock.ANY,
                            "option": mock.ANY,
                        },
                        {
                            "address": "1pasopso",
                            "number": "3412",
                            "postal_code": mock.ANY,
                            "province": mock.ANY,
                            "state": mock.ANY,
                            "status": mock.ANY,
                            "option": mock.ANY,
                        },
                    ]
                },
            ),
        )

        for label, sql in test_cases:
            with self.subTest(mgs=label):
                client = mock.MagicMock()
                collection = client['company']['employees']
                collection.fin.return_value = sql
                with patch('builtins.print') as mock_print:
                    get_sql()
