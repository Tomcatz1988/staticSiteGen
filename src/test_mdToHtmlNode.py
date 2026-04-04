import unittest
from mdToHtmlNode import mdToHtmlNode


class TestMdToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = mdToHtmlNode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = mdToHtmlNode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_quotes(self):
        md = """
>This is **bolded** paragraph
> text in a p
>tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = mdToHtmlNode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is <b>bolded</b> paragraph text in a p tag here</blockquote><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_header(self):
        md = """
# this is a single header

### this is triple header
"""

        node = mdToHtmlNode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is a single header</h1><h3>this is triple header</h3></div>",
        )


    def test_uoList(self):
        md = """
- This is **bolded** paragraph
- text in a p
- tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = mdToHtmlNode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is <b>bolded</b> paragraph</li><li>text in a p</li><li>tag here</li></ul><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_ordList(self):
        md = """
1. This is **bolded** paragraph
2. text in a p
3. tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = mdToHtmlNode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is <b>bolded</b> paragraph</li><li>text in a p</li><li>tag here</li></ol><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
