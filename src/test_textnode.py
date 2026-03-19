import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diff_texttype(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff_text_val(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2= TextNode("This is a bold node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.LINK, url="www.internet.com")
        node2 = TextNode("This is a text node", TextType.LINK, url="www.internet.com")
        self.assertEqual(node, node2)

    def test_diff_url(self):
        node = TextNode("This is a text node", TextType.LINK, url="www.internet.com")
        node2 = TextNode("This is a text node", TextType.LINK, url="www.outernet.com")
        self.assertNotEqual(node, node2)

    def test_null_url(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, url="www.outernet.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
