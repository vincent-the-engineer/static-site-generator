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


    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Leaf nodes must have a value.")
        if not self.tag:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
