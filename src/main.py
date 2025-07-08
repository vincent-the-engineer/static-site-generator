from textnode import TextNode, TextType

def main():
    node = TextNode("Test", TextType.BOLD)
    print(node)
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()
