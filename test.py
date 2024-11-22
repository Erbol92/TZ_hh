import unittest
from job_with_json import get_id


class TestGetId(unittest.TestCase):
    data = [
        {
            "author": "a1",
            "title": "t",
            "year": 2024,
            "status": "\u0432\u044b\u0434\u0430\u043d\u0430",
            "id": 1
        },
        {
            "author": "a2",
            "title": "t2",
            "year": 2024,
            "status": "n",
            "id": 2
        },
        {
            "author": "gogol",
            "title": "gore",
            "year": 2018,
            "status": "\u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438",
            "id": 3
        }
    ]

    def test_list(self):
        self.assertEqual(get_id(self.data), 4)

    def test_empty(self):
        self.assertEqual(get_id([]), 1)


if __name__ == '__main__':
    unittest.main()
