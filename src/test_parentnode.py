import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class testParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_gc_link(self):
        grandchild_node = LeafNode("a", "grandchild", {"href": "https://www.google.com"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><a href=\"https://www.google.com\">grandchild</a></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1_node = LeafNode("b", "child 1")
        child2_node = LeafNode("i", "child 2")
        child3_node = LeafNode(None, "child 3")
        parent_node = ParentNode("p", [child1_node, child2_node, child3_node])
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>child 1</b><i>child 2</i>child 3</p>"
        )

    def test_to_html_with_tree(self):
        grandchild1_node = LeafNode(None, "text 1")
        grandchild2_node = LeafNode("b", "bold")
        grandchild3_node = LeafNode("i", "italic") 
        child1_node = ParentNode("p", [grandchild1_node, grandchild2_node, grandchild3_node])
        child2_node = LeafNode("img", "image", {"src": "https://www.imgur.com", "alt": "This is an image"})
        grandchild4_node = LeafNode("i", "image description")
        grandchild5_node = LeafNode("a", "link description", {"href": "https://www.google.com"})
        child3_node = ParentNode("p", [grandchild4_node, grandchild5_node])
        parent_node = ParentNode("p", [child1_node, child2_node, child3_node])
        self.maxDiff = None
        self.assertEqual(
            parent_node.to_html(),
            "<p><p>text 1<b>bold</b><i>italic</i></p><img src=\"https://www.imgur.com\" alt=\"This is an image\" /><p><i>image description</i><a href=\"https://www.google.com\">link description</a></p></p>"
        )


if __name__ == "__main__":
    unittest.main()
