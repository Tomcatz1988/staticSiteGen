import unittest
from blocktype import BlockType, blockToBlockType


class test_BlockType(unittest.TestCase):
    def test_singleHeading(self):
        block = "# This is a single heading"
        block_type = blockToBlockType(block)
        self.assertEqual(block_type, BlockType.HEADING)


    def test_multipleHeading(self):
        block = "###### This is a single heading"
        block_type = blockToBlockType(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_incorrectHeading(self):
        block = "####### This is a single heading"
        block_type = blockToBlockType(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_codeBlock(self):
        block = """```
This is a code block.
```"""
        block_type = blockToBlockType(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_incorrectCodeBlock(self):
        block = """```
This is not a code block."""
        block_type = blockToBlockType(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_QuoteBlock(self):
        block = """> This is a quote block.
>This is a quote with no space
> This is still a quote block"""
        block_type = blockToBlockType(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_incorrectQuoteBlock(self):
        block = """> This quote block
is invalid"""
        block_type = blockToBlockType(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_UOListBlock(self):
        block = """- This is a list block.
- This is a list block"""
        block_type = blockToBlockType(block)
        self.assertEqual(block_type, BlockType.UO_LIST)

    def test_incorrectUOListBlock(self):
        block = """- This is a list block.
-This is not a list block"""
        block_type = blockToBlockType(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordListBlock(self):
        block = """1. This is a list block.
2.  This is a list block
3.This is a list block"""
        block_type = blockToBlockType(block)
        self.assertEqual(block_type, BlockType.ORD_LIST)

    def test_incorrectOrdListBlock(self):
        block = """1. This is a list block.
3.  This is a list block
2.This is a list block"""
        block_type = blockToBlockType(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
