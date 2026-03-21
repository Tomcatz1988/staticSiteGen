class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("HTMLNode.to_html has not been implemented")

    def props_to_html(self):
        if self.props == None:
            return ""
        props_string = ""
        for prop in self.props:
            props_string += f" {prop}=\"{self.props[prop]}\""
        return props_string

    def __repr__(self):
        return f"(HTMLNode)tag:\'{self.tag}\' / val:\'{self.value}\' / children:\'{self.children}\' / props:\'{self.props}\'" 
