import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnToFr(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Love"), {'translations': [{'translation': 'Amour'}], 'word_count': 1, 'character_count': 4})
        self.assertNotEqual(englishToFrench("Hello"), {'translations': [{'translation': 'animaux'}], 'word_count': 1, 'character_count': 5})

class TestFrToEn(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonne"), {'translations': [{'translation': 'Good'}], 'word_count': 1, 'character_count': 5})
        self.assertNotEqual(frenchToEnglish("animaux"), {'translations': [{'translation': 'Good'}], 'word_count': 1, 'character_count': 5})

unittest.main()