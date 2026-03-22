import unittest
from htmlnode import LeafNode


class testLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click Me!</a>")

    def test_leaf_to_html_plain_text(self):
        node = LeafNode(None, "plain text")
        self.assertEqual(node.to_html(), "plain text")


if __name__ == "__main__":
    unittest.main()
