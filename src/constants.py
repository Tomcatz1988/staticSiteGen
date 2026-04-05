from textnode import TextType


INLINE_DELIMITER_MAP = {
    "**": TextType.BOLD,
    "_": TextType.ITALIC,
    "`": TextType.CODE,
}

INLINE_TEXT_TYPE = (
    TextType.TEXT, 
    TextType.BOLD, 
    TextType.ITALIC, 
    TextType.CODE
)
