from enum import Enum
from textnode import TextNode
from textnode import TextType

def main():
    text = "this is text"
    text_type = TextType.BOLD_TEXT
    url = "https://www.aq.com"
    Sample = TextNode(text, text_type, url)
    print(Sample)


if __name__ == "__main__":
    main()