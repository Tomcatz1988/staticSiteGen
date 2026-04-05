import unittest
from texttonode import extractMarkdownImages, extractMarkdownLinks


class testExtractFromMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extractMarkdownImages(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extractMarkdownLinks(
            "This is text with an [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)
