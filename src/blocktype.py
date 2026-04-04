from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UO_LIST = "uo_list"
    ORD_LIST = "ord_list"


def isHeading(word, depth):
    word_len = len(word)
    if word_len > 6:
        return False
    if word[0] == '#':
        if word_len > 1:
            return isHeading(word[1:], depth + 1)
        return True


def isCodeBlock(first_line, last_line):
    return (first_line == "```") and (last_line == "```")


def isQuoteBlock(lines):
    if lines[0] != "":
        if lines[0][0] == '>':
            return True if len(lines) == 1 else isQuoteBlock(lines[1:])
    return False


def isUOListBlock(lines):
    first_word = lines[0].split(" ")
    if first_word[0] == '-':
        return True if len(lines) == 1 else isUOListBlock(lines[1:])
    return False


def isOrdListBlock(lines, count):
    first_word = lines[0].split('.')
    if first_word[0].isdigit():
        if int(first_word[0]) == count:
            return True if len(lines) == 1 else isOrdListBlock(lines[1:], count + 1)
    return False

        
def blockToBlockType(block):
    lines = block.split('\n')
    lines_len = len(lines)
    if isHeading(lines[0].split(" ")[0], 0):
        return BlockType.HEADING
    if lines_len > 1:
        if isCodeBlock(lines[0], lines[lines_len - 1]):
            return BlockType.CODE
    if isQuoteBlock(lines):
        return BlockType.QUOTE
    if isUOListBlock(lines):
        return BlockType.UO_LIST
    if isOrdListBlock(lines, 1):
        return BlockType.ORD_LIST
    return BlockType.PARAGRAPH
