from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node has no value")
        html = ""
        match self.tag:        
            case None:
                html = f"{self.value}"
            case "img":
                html = f"<{self.tag}{self.props_to_html()} />"
            case _:
                html = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return html


    def __repr__(self):
        return f"(HTMLNode)tag:\'{self.tag}\' / val:\'{self.value}\' / props:\'{self.props}\'" 
