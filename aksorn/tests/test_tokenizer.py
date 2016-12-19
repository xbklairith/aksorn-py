import unittest
from aksorn.tokenizer import tokenizer
class TestMain(unittest.TestCase):
	def setUp(self):
		print("setup")

	def test_tokenizer(self):
		tokenizer.tokenize('การเขียนเรียงความ')



if __name__ == '__main__':
    unittest.main()