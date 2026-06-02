import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
gc = HTMLNode("Hey I exist too")
child = HTMLNode("it worked", children=[gc])
parent = HTMLNode("testing node...", None, children=[child])
class TestHtmlNode(unittest.TestCase):
    def test_f(self):
        node1 = HTMLNode("p", parent, child, {"this": "is a pair", "target": "am lost",})
        node2 = HTMLNode("strong", parent, child, {"the family": "grows in number",})
        node3 = HTMLNode("a", parent, None, {"I":"could not be clever",})
        print(node1)
        print(node2)
        print(node3)
        self.assertEqual(node1.props_to_html(), ' this="is a pair" target="am lost"')
        self.assertNotEqual(node2.props_to_html(), ' this="is a pair" target="am lost"')
        self.assertEqual(node3.props_to_html(), ' I="could not be clever"')
    
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, Grim!")
        node2 = LeafNode("strong", "DMC3 is peak")
        node3 = LeafNode("a", "Click me!", {"href": "https://google.com"})
        print(node)
        print(node2)
        print(node3)
        self.assertEqual(node.to_html(), "<p>Hello, Grim!</p>")
        self.assertNotEqual(node2.to_html(), "<strong> DMC2 is peak</strong>")
        self.assertEqual(node3.to_html(), '<a href="https://google.com">Click me!</a>')
if __name__ == "__main__":
    unittest.main()