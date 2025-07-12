import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodes_Delimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
            ]
        )

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ]
        )

    def test_italic(self):
        node = TextNode("This is text ending with _italic phrase_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text ending with ", TextType.TEXT),
            TextNode("italic phrase", TextType.ITALIC),
            ]
        )

    def test_multiple_bold(self):
        node = TextNode("This has **bolded phrase 1** and **bold2**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This has ", TextType.TEXT),
            TextNode("bolded phrase 1", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold2", TextType.BOLD),
            ]
        )

    def test_no_closing_tag(self):
        node = TextNode("Testing **no bold phrase", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("Testing ", TextType.TEXT),
            TextNode("no bold phrase", TextType.TEXT),
            ]
        )

    def test_no_tag(self):
        node = TextNode("This has no tags.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This has no tags.", TextType.TEXT),
            ]
        )

    def test_single_item(self):
        node = TextNode("**bolded text only**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("bolded text only", TextType.BOLD),
            ]
        )

    def test_multiple_nodes(self):
        node1 = TextNode("This is `code block` word", TextType.TEXT)
        node2 = TextNode("This is **bold word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is **bold word**", TextType.TEXT),
            ]
        )

    def test_chaining(self):
        node1 = TextNode("This is `code block` word", TextType.TEXT)
        node2 = TextNode("This is **bold word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is ", TextType.TEXT),
            TextNode("bold word", TextType.BOLD),
            ]
        )


