import re

from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old_node)
        elif old_node.text_type == TextType.PLAIN_TEXT:
            parts = old_node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception("invalid markdown")
            for i, part in enumerate(parts):
                if part == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.PLAIN_TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes

#break to extracting images and links
def extract_markdown_images(text):
    return re.findall(r"!\[([^\]]+)\]\(([^\)]+)\)", text)
    

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\]]+)\]\(([^\)]+)\)", text)

#back to splitting

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.PLAIN_TEXT:
            leftover = old_node.text
            image_pieces = extract_markdown_images(old_node.text)
            if len(image_pieces) == 0:
                new_nodes.append(old_node)
                continue
            for alt, url in image_pieces:
                markdown = f"![{alt}]({url})"
                before, after = leftover.split(markdown, 1)
                if before != "":
                    new_nodes.append(TextNode(before, TextType.PLAIN_TEXT))
                new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                leftover = after
            if leftover != "":
                new_nodes.append(TextNode(leftover, TextType.PLAIN_TEXT))
        else:
            new_nodes.append(old_node)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old_node)
            continue
        leftover = old_node.text
        link_pieces = extract_markdown_links(old_node.text)
        if len(link_pieces) == 0:
            new_nodes.append(old_node)
            continue
        for anchor, url in link_pieces:
            markdown = f"[{anchor}]({url})"
            before, after = leftover.split(markdown, 1)
            if before != "":
                new_nodes.append(TextNode(before, TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(anchor, TextType.LINK, url))
            leftover = after
        if leftover != "":
            new_nodes.append(TextNode(leftover, TextType.PLAIN_TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.PLAIN_TEXT)]
    
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC_TEXT)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    
    return nodes