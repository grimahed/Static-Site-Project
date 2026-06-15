import unittest
from blocktypes import *
from htmlnode import *
from textnode import *
from split_nodes_delimiter import *

class test_blocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        #md inputs
        md = """
This is a **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- this is a list
- with items
"""

        md2 = """
**If you say DMC3 is peak again I'm banning you from coffee**
_You can't stop me I'm the one writing you! DMC3 is peak._


"""
#actual tests
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- this is a list\n- with items",
            ]
        )

        blocks2 = markdown_to_blocks(md2)
        self.assertEqual(
            blocks2,
            [
                "**If you say DMC3 is peak again I'm banning you from coffee**\n_You can't stop me I'm the one writing you! DMC3 is peak._",
            ]
        )

    def test_find_block_type(self):
        md = """1. This is
2. An ordered list
3. extended though
4. can we go much lowerrrr
5. wait don't you mean higher? look at the number
6. Dunno...didn't think I'd get this far"""

        md2 = """- This is
- unordered.
- ya don't say?
- I should probably finish my laundry at some point.
- GW3 announced pog"""


        md3 = """# This is one heading
```Hey guys, where's the bathroom?```
##ayo who are you"""

        md4 = """> Say the line bart
> DMC3 is the best Hack n' Slash game
> the classroom cheers"""

        block = block_to_block_type(md)
        self.assertEqual(block,
            BlockType.ORDERED_LIST
        )

        block2 = block_to_block_type(md2)
        self.assertEqual(block2,
            BlockType.UNORDERED_LIST
        )

        block3 = block_to_block_type(md3)
        self.assertNotEqual(block3,
            BlockType.CODE
        )

        block4 = block_to_block_type(md4)
        self.assertEqual(block4,
            BlockType.QUOTE
        )

    def test_block_to_html(self):
    ####UNORDERED LIST
        md = """
- This is
- an
- unordered list"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is</li><li>an</li><li>unordered list</li></ul></div>",
        )
 
    ####ORDERED LIST
        md2 = """
1. I'm gonna say it
2. DMC2 is good actually
3. What, thought I was gonna say the thing about DMC, huh?"""

        node2 = markdown_to_html_node(md2)
        html2 = node2.to_html()
        self.assertEqual(
            html2,
            "<div><ol><li>I'm gonna say it</li><li>DMC2 is good actually</li><li>What, thought I was gonna say the thing about DMC, huh?</li></ol></div>"
        )

    ####PARAGRAPH
        md3 = """This is a paragraph.
This is still a paragraph.
Yep. Still a paragraph"""

        node3 = markdown_to_html_node(md3)
        html3 = node3.to_html()
        self.assertEqual(
            html3,
            "<div><p>This is a paragraph. This is still a paragraph. Yep. Still a paragraph</p></div>"
        )
        
        md4 = """#### This is a fourth heading."""

        node4 = markdown_to_html_node(md4)
        html4 = node4.to_html()
        self.assertEqual(
            html4,
            "<div><h4>This is a fourth heading.</h4></div>"
        )

        md5 = """
```
This
is code
```
"""
        node5 = markdown_to_html_node(md5)
        html5 = node5.to_html()
        self.assertEqual(
            html5,
            "<div><pre><code>This\nis code\n</code></pre></div>"
        )

        md6 = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node6 = markdown_to_html_node(md6)
        html6 = node6.to_html()
        self.assertEqual(
            html6,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
        md7 = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node7 = markdown_to_html_node(md7)
        html7 = node7.to_html()
        self.assertEqual(
            html7,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

        print("---BLOCK TO HTML TESTING---\n")
        print(html)
        print(html2)
        print(html3)
        print(html4)
        print(html5)
        print(html6)
        print(html7)
        print("\n-----------------\n")
    
