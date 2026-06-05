import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from textnode import *
gc = HTMLNode("Hey I exist too")
child = HTMLNode("it worked", children=[gc])
parent = HTMLNode("testing node...", None, children=[child])
class TestHtmlNode(unittest.TestCase):
    def test_f(self):
        node1 = HTMLNode("p", parent, child, {"this": "is a pair", "target": "am lost",})
        node2 = HTMLNode("strong", parent, child, {"the family": "grows in number",})
        node3 = HTMLNode("a", parent, None, {"I":"could not be clever",})

        print("---HTMLNode Tests---\n")
        print(node1)
        print(node2)
        print(node3)
        print("\n------------------\n")
        self.assertEqual(node1.props_to_html(), ' this="is a pair" target="am lost"')
        self.assertNotEqual(node2.props_to_html(), ' this="is a pair" target="am lost"')
        self.assertEqual(node3.props_to_html(), ' I="could not be clever"')
    
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, Grim!")
        node2 = LeafNode("strong", "DMC3 is peak")
        node3 = LeafNode("a", "Click me!", {"href": "https://google.com"})
        print("---LEAFNode tests---\n")
        print(node)
        print(node2)
        print(node3)
        print("\n------------------\n")
        self.assertEqual(node.to_html(), "<p>Hello, Grim!</p>")
        self.assertNotEqual(node2.to_html(), "<strong> DMC2 is peak</strong>")
        self.assertEqual(node3.to_html(), '<a href="https://google.com">Click me!</a>')

    def test_to_html_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        print("---Child node test(s)---\n")
        print(parent_node)
        print("\n------------------\n")
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_grandchildren(self):
        #gc_n = grandchild node

        gc_n = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [gc_n])
        parent_node = ParentNode("div", [child_node])
        print("---GRANDchild node (no prop) test(s)---\n")
        print(parent_node)
        print("\n------------------\n")
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_gc_prop(self):
         #gc_n = grandchild node

        gc_n = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [gc_n], {"href": "https://google.com"})
        parent_node = ParentNode("div", [child_node])
        print("---Grandchild node WITH prop tests---\n")
        print(parent_node)
        print("\n-----------------\n")
        self.assertEqual(
            parent_node.to_html(),
            '<div><span href="https://google.com"><b>grandchild</b></span></div>',
        )

    def test_to_html_great_grandchildren(self):
        #ggc_n = greatgrandchild node, so on.

        ggc_n = LeafNode("strong", "great-grandchild")
        gc_n = ParentNode("b", [ggc_n])
        child_node = ParentNode("span", [gc_n])
        parent_node = ParentNode("div", [child_node])
        print("---GGC node Test---\n")
        print(parent_node)
        print("\n-----------------\n")
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><strong>great-grandchild</strong></b></span></div>",
        )

    def test_to_html_great_grandchildren_prop(self):
        #ggc_n = greatgrandchild node, so on.

        ggc_n = LeafNode("strong", "great-grandchild")
        gc_n = ParentNode("b", [ggc_n])
        child_node = ParentNode("span", [gc_n])
        parent_node = ParentNode("div", [child_node], {"href": "https://google.com"})
        print("---GGC node w/prop Test---\n")
        print(parent_node)
        print("\n-----------------\n")
        self.assertEqual(
            parent_node.to_html(),
            '<div href="https://google.com"><span><b><strong>great-grandchild</strong></b></span></div>',
        )


        #TEXT NODE TESTS HERE
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        node2 = TextNode("This is also a test node", TextType.BOLD_TEXT)
        node3 = TextNode("DMC3 is peak", TextType.ITALIC_TEXT)
        node4 = TextNode("ALRIGHT WE GET IT", TextType.CODE_TEXT)
        node5 = TextNode("this is text", TextType.LINK, {"href": "https://google.com"})
        node6 = TextNode("This is text", TextType.IMAGE, "https://google.com/images")
        html_node = text_node_to_html_node(node)
        html_node2 = text_node_to_html_node(node2)
        html_node3 = text_node_to_html_node(node3)
        html_node4 = text_node_to_html_node(node4)
        html_node5 = text_node_to_html_node(node5)
        html_node6 = text_node_to_html_node(node6)
        print("---TEXT nodes to html node tests---\n")
        print(html_node)
        print(html_node2)
        print(html_node3)
        print(html_node4)
        print(html_node5)
        print(html_node6)
        print("\n-----------------\n")
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node2.tag, "b")
        self.assertEqual(html_node2.value, "This is also a test node")
        self.assertEqual(html_node3.tag, "i")
        self.assertEqual(html_node3.value, "DMC3 is peak")
        self.assertEqual(html_node4.tag, "code")
        self.assertEqual(html_node4.value, "ALRIGHT WE GET IT")
        self.assertEqual(html_node5.tag, "a")
        self.assertEqual(html_node5.props_to_html(), ' href="https://google.com"')
        self.assertEqual(html_node6.tag, "img")
        self.assertEqual(html_node6.props_to_html(), ' https://google.com/images="This is text"')
if __name__ == "__main__":
    unittest.main()