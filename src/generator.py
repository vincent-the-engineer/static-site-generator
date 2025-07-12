from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str,
                          text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        # No current support for nested inline TextType.
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        in_tag = False
        while text:
            index = text.find(delimiter)
            if index >= 0:
                head = text[:index]
                text = text[index + len(delimiter):]
                if head:
                    if in_tag:
                        new_nodes.append(TextNode(head, text_type))
                    else:
                        new_nodes.append(TextNode(head, TextType.TEXT))
                in_tag = not in_tag
            else:
                # No tag means plain text.
                new_nodes.append(TextNode(text, TextType.TEXT))
                text = ""
    return new_nodes

