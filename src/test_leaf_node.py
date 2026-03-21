import unittest
from leafnode import LeafNode


class testLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        print(node)
        print(node.to_html())
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click Me!</a>")

if __name__ == "__main__":
    unittest.main()
