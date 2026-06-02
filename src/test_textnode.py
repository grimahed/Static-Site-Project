import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a test node", TextType.BOLD_TEXT)
        node3 = TextNode("This is a test node", TextType.ITALIC_TEXT)
        node4 = TextNode("this is a test node", TextType.CODE_TEXT)
        node5 = TextNode("this is a test node", TextType.PLAIN_TEXT)
        node6 = TextNode(None, TextType.LINK)
        node7 = TextNode("this is a test node image.jpeg", TextType.IMAGE)
        node8 = TextNode("fooled you, back to JS purgatory", TextType.LINK, "https://www.aq.com/")
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node4, node5)
        self.assertNotEqual(node6, node7)
        self.assertNotEqual(node6, node8)
if __name__ == "__main__":
    unittest.main()