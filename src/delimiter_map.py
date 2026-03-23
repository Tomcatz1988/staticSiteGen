from textnode import TextType

inline_delimiter_map ={
    "**": TextType.BOLD,
    "_": TextType.ITALIC,
    "`": TextType.CODE,
}

inline_text_type = (
    TextType.TEXT, 
    TextType.BOLD, 
    TextType.ITALIC, 
    TextType.CODE
)
