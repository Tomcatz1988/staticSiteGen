import unittest
from htmlnode import HTMLNode


class testHTMLNode(unittest.TestCase):
    def test_props(self):
        test_prop = {
           "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=test_prop)
        expected_string = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(expected_string, node.props_to_html())

    def test_empty_props(self):
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())

    def test_tag_init(self):
        test_tag = "<p>"
        node = HTMLNode(tag=test_tag)
        print(node)
        self.assertEqual(node.tag, test_tag)
    
    def test_value_init(self):
        test_val = "This would be inside of a paragraph"
        node = HTMLNode(value=test_val)
        print(node)
        self.assertEqual(node.value, test_val)

    def test_children_init(self):
        test_children = [HTMLNode(tag=f"{i}") for i in range(3)]
        node = HTMLNode(children=test_children)
        self.assertEqual(node.children, test_children)
