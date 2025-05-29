from enum import Enum
from htmlnode import ParentNode, LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self,other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        type = TextType(self.text_type).vaule
        return f"TextNode({self.text}, {type}, {self.url})"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC:
            return LeafNode("i",text_node.text)
        case TextType.CODE:
            return LeafNode("code",text_node.text)
        case TextType.LINK:
            return LeafNode("a",text_node.text,{"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img","",{"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("unknown text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            text_list.append(node.text)
        elif node.text.count(delimiter) % 2 == 1:
            raise SyntaxError("invalid Markdown syntax")
        else:
            split_list = node.text.split(delimiter)
            for i in range(len(split_list)):
                if i%2 == 0:
                    text_list.append(TextNode(split_list[i],TextType.TEXT))
                else:
                    text_list.append(TextNode(split_list[i],text_type))
    return text_list
