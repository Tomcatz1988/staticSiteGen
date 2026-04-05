import unittest
from htmlnode import LeafNode


class testLeafNode(unittest.TestCase):
    def test_leaf_toHtml_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.toHtml(), "<p>Hello, World!</p>")

    def test_leaf_toHtml_a(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(node.toHtml(), "<a href=\"https://www.google.com\">Click Me!</a>")

    def test_leaf_toHtml_plain_text(self):
        node = LeafNode(None, "plain text")
        self.assertEqual(node.toHtml(), "plain text")


if __name__ == "__main__":
    unittest.main()
