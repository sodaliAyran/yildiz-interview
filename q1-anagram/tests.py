import unittest
from q1_anagram import anagram

class TestAnagram(unittest.TestCase):

    def test_same_word(self):
        res1, res2 = anagram("ilke", "ilke")
        self.assertEqual(res1 + res2, 0)

    def test_anagram(self):
        res1, res2 = anagram("ilke", "ekil")
        self.assertEqual(res1 + res2, 0)

    def test_sentence_one(self):
        res1, res2 = anagram("Tom Marvolo Riddle", "I Am Lord Voldemort")
        self.assertEqual(res1, 7)
        self.assertEqual(res2, 8)

    def test_sentence_two(self):
        res1, res2 = anagram("tom marvolo riddle", "i am lord voldemort")
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 1)

    def test_sentence_three(self):
        res1, res2 = anagram("tom marvolo riddle", "i am lordvoldemort")
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)

    def test_sentence_four(self):
        res1, res2 = anagram("tom riddle", "voldemort")
        self.assertEqual(res1, 3)
        self.assertEqual(res2, 2)

if __name__ == '__main__':
    unittest.main()
