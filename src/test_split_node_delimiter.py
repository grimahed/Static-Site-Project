import unittest
from split_nodes_delimiter import *
from htmlnode import *
from textnode import *

class test_split_delimiter(unittest.TestCase):

    def test_delimiter(self):
        node = TextNode("This is text with a 'code block' word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "'", TextType.CODE_TEXT)

        node2 = TextNode("This is text with **YELLING** text", TextType.PLAIN_TEXT)
        new_nodes2 = split_nodes_delimiter([node2], "**", TextType.BOLD_TEXT)

        node3 = TextNode("_I am stressing this statement_", TextType.PLAIN_TEXT)
        new_node3 = split_nodes_delimiter([node3], "_", TextType.ITALIC_TEXT)

        node4 = TextNode("**Day 5, they still haven't noticed(we did)", TextType.PLAIN_TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node4], "**", TextType.BOLD_TEXT)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" word", TextType.PLAIN_TEXT),
            ]
        )

        self.assertEqual(new_nodes2, [
            TextNode("This is text with ", TextType.PLAIN_TEXT),
            TextNode("YELLING", TextType.BOLD_TEXT),
            TextNode(" text", TextType.PLAIN_TEXT)
            ]
        )
        self.assertEqual(new_node3, [
            TextNode("I am stressing this statement", TextType.ITALIC_TEXT)
            ]
        )

        print("---Delimiter tests---\n")
        print(new_nodes)
        print(new_nodes2)
        print(new_node3)
        print(node4)
        print("\n------------------\n")

    def test_image_extraction(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        print("---image extraction test---\n")
        print(matches)
        print("\n-----------------\n")

    def test_link_extraction(self):
        matches2 = extract_markdown_links(
        "There's a [link](https://google.com) deleting me. rude."
        )
        self.assertListEqual([("link", "https://google.com")], matches2)
        print("---link extraction test---\n")
        print(matches2)
        print("\n-----------------\n")

    #splitting image and link tests
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://google.com) and another [second link](https://google.com)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://google.com"
                ),
            ],
            new_nodes,
        )
    
    def test_text_to_textnode(self):
        node = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        node2 = text_to_textnodes("**I AM VERY ANGRY >:C**")
        node3 = text_to_textnodes("_If your coffee is considered drinkable by your coworkers, it ain't strong enough_")
        node4 = text_to_textnodes("`Bear witness to the best hack n' slash game and also a very long link because I'm lazy` ![godammit why are you like this](https://static.wikia.nocookie.net/devilmaycry/images/a/ae/Devil_May_Cry_3_Cover_Art_Japan.jpg/revision/latest/scale-to-width/360?cb=20250423043714)")
        self.assertListEqual(
            [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType. PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.PLAIN_TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN_TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"
            ),
            ],
            node,
        )

        self.assertListEqual(
            [
            TextNode("I AM VERY ANGRY >:C", TextType.BOLD_TEXT)
            ],
            node2
        )

        self.assertListEqual(
            [
            TextNode("If your coffee is considered drinkable by your coworkers, it ain't strong enough", TextType.ITALIC_TEXT)
            ],
            node3
        )
        self.assertListEqual(
            [
            TextNode("Bear witness to the best hack n' slash game and also a very long link because I'm lazy", TextType.CODE_TEXT),
            TextNode(" ", TextType.PLAIN_TEXT),
            TextNode("godammit why are you like this", TextType.IMAGE, "https://static.wikia.nocookie.net/devilmaycry/images/a/ae/Devil_May_Cry_3_Cover_Art_Japan.jpg/revision/latest/scale-to-width/360?cb=20250423043714")
            ],
            node4
        )
        
        print("---TEXT TO NODE CONVERSION TESTS---\n")
        print(f"{node}\n")
        print(f"{node2}\n")
        print(f"{node3}\n")
        print(f"{node4}\n")
        print("\n-------------\n")

if __name__ == "__main__":
    unittest.main()