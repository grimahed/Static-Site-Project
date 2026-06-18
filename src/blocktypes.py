from enum import Enum
from htmlnode import *
from textnode import *
from split_nodes_delimiter import *


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

#BLOCK CREATION
def markdown_to_blocks(markdown):
    block = markdown.split("\n\n")
    split_block = []
    for line in block:
        new_line = line.strip()
        if new_line != "":
            split_block.append(new_line)
    return split_block

def block_to_block_type(block):
    first_line = 1
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    elif block.startswith("#"):
        count = 1
        while count < len(block) and block[count] == "#":
            count += 1
        if 1 <= count <= 6 and count < len(block) and block[count] == " ":
            return BlockType.HEADING
    
    elif block.startswith(">"):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
       
    elif block.startswith(f"{first_line}. "):
        lines = block.split("\n")
        for l, line in enumerate(lines, start=1):
            if not line.startswith(f"{l}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    
    elif block.startswith(f"- "):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(f"- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    return BlockType.PARAGRAPH
    
    #converting markdown to html nodes
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            block_node = paragraph_to_html(block)
            block_nodes.append(block_node)
        elif block_type == BlockType.UNORDERED_LIST:
            block_node = unordered_list_to_html(block)
            block_nodes.append(block_node)
        elif block_type == BlockType.ORDERED_LIST:
            block_node = ordered_list_to_html(block)
            block_nodes.append(block_node)
        elif block_type == BlockType.CODE:
            block_node = code_to_html(block)
            block_nodes.append(block_node)
        elif block_type == BlockType.HEADING:
            block_node = heading_to_html(block)
            block_nodes.append(block_node)
        elif block_type == BlockType.QUOTE:
            block_node = quote_to_html(block)
            block_nodes.append(block_node)
    return ParentNode("div", block_nodes, None)


#helper functions
def text_to_children(text):
    HTML_nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        HTML_nodes.append(text_node_to_html_node(node))
    return HTML_nodes

def paragraph_to_html(block):
    block_text = block.replace("\n", " ")
    block_child = text_to_children(block_text)
    return ParentNode("p", block_child, None)
        
def ordered_list_to_html(block):
    li_nodes = []

    lines = block.split("\n")
    for l, line in enumerate(lines, start=1):
        prefix = f"{l}. "
        item_text = line[len(prefix):]
        item_children = text_to_children(item_text)
        li_node = ParentNode("li", item_children, None)
        li_nodes.append(li_node)
    return ParentNode("ol", li_nodes, None)

def unordered_list_to_html(block):
    li_nodes = []
    lines = block.split("\n")
    for line in lines:
        line_text = line[2:]
        line_children = text_to_children(line_text)
        li_node = ParentNode("li", line_children, None)
        li_nodes.append(li_node)
    return ParentNode("ul", li_nodes, None)

def heading_to_html(block):
    level = 0
    while block[level] == "#":
        level += 1
    block_text = block[level + 1:]
    heading_child = text_to_children(block_text)
    return ParentNode(f"h{level}", heading_child, None)

def quote_to_html(block):

    new_lines = []
    lines = block.split("\n")
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children, None)
    
def code_to_html(text):
    code_text = text[4:-3]
    text_node = TextNode(code_text, TextType.PLAIN_TEXT, None)
    child = text_node_to_html_node(text_node)
    code_node = ParentNode("code", [child], None)
    return ParentNode("pre", [code_node], None)