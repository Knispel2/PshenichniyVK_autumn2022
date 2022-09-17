import unittest
import sys
import os
import random
from mock import MagicMock
from faker import Faker
import json_proj


class TestJSON(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = json_proj.parse_json
        sys.stdout = open(os.devnull, 'w', encoding='utf8')

    def test_manual(self):
        base_json = '''{
        "names":"John|Peter|Vasa|Vera|Katya",
        "ages":"20|28|21|27|26",
        "city":"Moscow|Krasnodar|Tomsk|Moskow",
        "job":"Builder|Office-Worker|Translator|Writer"
        }'''
        fake_func = MagicMock(name = 'Test')
        fake_func.return_value = None
        self.obj(base_json, ['names', 'ages'], ['Vasa', '20'], fake_func)
        self.assertEqual(fake_func.call_count, 2)

    def test_auto(self):
        self.obj = json_proj.parse_json
        fake_generator = Faker('en_US')
        for i in range(300):
            num_tests = random.randint(1, 10)
            base_names = [fake_generator.name().split(' ')[0] for i in range(30)]
            base_jobs = [str(fake_generator.job()) for i in range(30)]
            base_ages = [str(fake_generator.unique.random_int()) for i in range(30)]
            base_json = '{' + f'''
"names":"{'|'.join(base_names)}",
"ages":"{'|'.join(base_ages)}",
"job":"{'|'.join(base_jobs)}"
''' + '}'
            fake_func = MagicMock(name = 'Test')
            fake_func.return_value = None
            fake_func.call_count = 0
            test_choice = set(random.choices(base_names + base_jobs + base_ages, k=num_tests))
            self.obj(base_json, ['names', 'ages', 'job'], list(test_choice), fake_func)
            self.assertEqual(fake_func.call_count, len(test_choice))

    def tearDown(self) -> None:
        sys.stdout.close()
        sys.stdout = sys.__stdout__
