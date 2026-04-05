import unittest
from genpage import extractTitle


class TestExtractTitle(unittest.TestCase):
    def test_valid_heading(self):
        html = "<h1>Here is a title</h1>"
        self.assertEqual(extractTitle(html), "Here is a title")


    def test_invaild_heading(self):
        html = "<p>No title present</p>"
        try:
            title = extractTitle(html)
        except Exception as e:
            self.assertEqual(str(e), "no valid heading for title generation")

