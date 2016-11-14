import unittest
import os
import Ejer3
from flask_testing import TestCase
import tempfile

class ejercicioTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, Ejer3.app.config['DATABASE'] = tempfile.mkstemp()
        Ejer3.app.config['TESTING'] = True
        self.app = Ejer3.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(Ejer3.app.config['DATABASE'])

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_name_status_code(self):
        result = self.app.get('/user/ruben')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
