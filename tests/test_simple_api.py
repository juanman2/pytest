import unittest
from simple_api import SimpleApi

class TestSimpleAPI(unittest.TestCase):

    
    createTests = [{'in' : {'v1': 'hello'}, 'result' : True},
                   {'in' : {'v1': 'hello', 'v2': 2.0}, 'result' : True},
                   {'in' : {'v1': 'hello', 'v2': 3, 'v3': True}, 'result' : False},
                   {'in' : {'v1': 999}, 'result' : False},
                   {'in' : {'v1': 1.2, 'v2': 3, 'v3': True}, 'result' : False},
                   {'in' : {'v1': 1.2, 'v2': 3, 'v3': "str"}, 'result' : False}
                   ]

    def setUp(self):
        self.sa = SimpleApi()
    
    def test_create(self):
        for t in self.createTests:
            try:
                self.sa.create(**t['in'])
                self.assertEqual(t['result'], True, 'Creating {:} Expected {:} but got {:}'.format(t,t['result'], True))
            except Exception as e:
                self.assertEqual(t['result'], False, 'Creating {:} Expected {:} but got {:}: {:}'.format(t,t['result'], False, e))
    

if __name__ == '__main__':
    unittest.main()

    
