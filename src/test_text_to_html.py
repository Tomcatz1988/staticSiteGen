import unittest
from text_to_html import *
from textnode import TextNode, TextType
from leafnode import LeafNode
from parentnode import ParentNode 


class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_to_html(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        text_node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_to_html(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        text_node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_to_html(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    def test_code(self):
        text_node = TextNode("This is a code node", TextType.CODE)
        html_node = text_to_html(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link_good(self):
        text_node = TextNode("This is a link node", TextType.LINK, "https://www.google.com")
        html_node = text_to_html(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_image_good(self):
        text_node = TextNode("This is an image node", TextType.IMAGE, "https://www.imgur.com")
        html_node = text_to_html(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.imgur.com", "alt": "This is an image node"})

    def test_link_no_url(self):
        text_node = TextNode("This is a link node", TextType.LINK)
        try:
            html_node = text_to_html(text_node)
        except Exception as e:
            self.assertEqual(str(e), str(Exception("cannot create HTMLNode <LINK> due to TextNode.url having None value")))

    def test_image_no_url(self):
        text_node = TextNode("This is an image node", TextType.IMAGE)
        try:
            html_node = text_to_html(text_node)
        except Exception as e:
            self.assertEqual(str(e), str(Exception("cannot create HTMLNode <IMAGE> due to TextNode.url having None value")))


if __name__ == "__main__":
    unittest.main()
