import unittest
import wetrans

class TestWetrans(unittest.TestCase):

    #@classmethod
    #def setUpClass(cls):
        # procedures before tests are started. This code block is executed only once

    #def tearDownClass(cls):
        # procedures after tests are finished. This code block is executed only once

    #def setUp(self):
        # procedures before every tests are started. This code block is executed every time

    #def tearDown(self):
        # procedures after every tests are finished. This code block is executed every time

    def test_translate(self):
        # one test case. here. 
        # You must 'test_' prefix always. Unless, unittest ignores
        #t = wetrans.wetrans.Translate()
        #aaa = t.translate("Hello")
        #print(aaa)
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
