import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        res = cap.cap_text(text)
        self.assertEqual(res,'Python')

    def test_multiple_words(self):
        text = 'hello there'
        res = cap.cap_text(text)
        self.assertEqual(res,'Hello there')

if __name__ == '__main__':
    unittest.main()