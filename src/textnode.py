from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    PLAIN_TEXT = "text"
    BOLD_TEXT = "bolded"
    ITALIC_TEXT = "italicized"
    CODE_TEXT = "code"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        #comparing self to other
        return (self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__(self):
        TEXT = self.text
        TEXT_TYPE = self.text_type.value
        URL = self.url
        return f"TextNode({TEXT}, {TEXT_TYPE}, {URL})"
    
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.PLAIN_TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE_TEXT:
        return LeafNode("code", text_node.text)  
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url}) 
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt":  text_node.text})
    else:
        raise Exception("invalid type")
    