class HTMLNode:
    def __init__(
            self,
            tag: str = None,
            value: str = None,
            children: list['HTMLNode'] = None,
            props: dict[str: str] = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def __repr__(self) -> str:
        return (
            f'HTMLNode({self.tag}, {self.value}, children: {self.children},'
            + f' {self.props})'
        )


    def to_html(self) -> str:
        raise NotImplementedError()


    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        props_list = []
        for key, value in self.props.items():
            props_list.append(f'{key}="{value}"')
        return " ".join(props_list)


class LeafNode(HTMLNode):
    def __init__(
            self,            
            tag: str,
            value: str,
            props: dict[str: str] = None) -> None:
        super().__init__(tag, value, None, props)


    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Leaf nodes must have a value.")
        if not self.tag:
            return self.value
        if self.props:
            props = " " + self.props_to_html()
        else:
            props = ""
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: list[HTMLNode],
            props: dict[str, str] = None) -> None:
        super().__init__(tag, None, children, props)


    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")
        if not self.children:
            raise ValueError("ParentNode must have children nodes.")
        children_html = []
        for child in self.children:
            children_html.append(child.to_html())
        return f"<{self.tag}>{"".join(children_html)}</{self.tag}>"
