import unittest
from src.preprocessing import TextPreprocessor

class TestPreprocessing(unittest.TestCase):
    def setUp(self):
        self.processor = TextPreprocessor()

    def test_clean_text(self):
        self.assertEqual(
            self.processor.clean_text("Hello! Visit https://example.com"),
            "hello visit"
        )

    def test_remove_stopwords(self):
        tokens = ["this", "is", "an", "example"]
        self.assertEqual(
            self.processor.remove_stopwords(tokens),
            ["example"]
        )

    def test_stem_tokens(self):
        tokens = ["running", "jumps", "easily"]
        self.assertEqual(
            self.processor.stem_tokens(tokens),
            ["run", "jump", "easili"]
        )

