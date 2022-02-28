from typing import Optional

import graphviz


def process_label(text: Optional[str]) -> Optional[str]:
    """Insert brackets around text.

    Parameters
    ----------
    text
        Text to be processed.

    Returns
    -------
    Optional[str]
        Processed text.
    """
    if text is not None:
        return f"<{text}>"
    else:
        return None


class ERD:
    """
    Parameters
    ----------
    gr
        A object from the graphviz.Graph class.

    Attributes
    ----------
    gr
        Graphviz object.
    """

    def __init__(self, gr: graphviz.Graph) -> None:
        self.gr = gr

    def entity(self, node_name: str, node_label: Optional[str] = None):
        """This method declares an entity.

        Parameters
        ----------
        node_name
            Name of the node.

        node_label
            Name that will appear at the node.
        """
        self.gr.node(node_name, process_label(node_label), shape="box")

    def weak_entity(self, node_name: str, node_label: Optional[str] = None):
        """This method declares a weak entity.

        Parameters
        ----------
        node_name
            Name of the node.

        node_label
            Name that will appear at the node.
        """
        self.gr.node(
            node_name,
            process_label(node_label),
            shape="box",
            peripheries="2",
        )

    def associative_entity(
        self, node_name: str, node_label: Optional[str] = None
    ):
        """This method declares an associative entity.

        Parameters
        ----------
        node_name
            Name of the node.

        node_label
            Name that will appear at the node.
        """

        self.gr.node(node_name, process_label(node_label), shape="Msquare")

    def attribute(self, node_name: str, node_label: Optional[str] = None):
        """This method declares an attribute.

        Parameters
        ----------
        node_name
            Name of the node.

        node_label
            Name that will appear at the node.
        """
        self.gr.node(node_name, process_label(node_label), shape="ellipse")

    def multivalue(self, node_name: str, node_label: Optional[str] = None):
        """This method declares a multivalued attribute.

        Parameters
        ----------
        node_name
            Name of the node.

        node_label
            Name that will appear at the node.
        """
        # self.gr.node(node_name, node_label, {"shape": "ellipse", "peripheries": "2"})
        self.gr.node(
            node_name,
            process_label(node_label),
            shape="ellipse",
            peripheries="2",
        )

    def key(self, node_name: str, node_label: Optional[str] = None):
        """This method declares a key attribute.

        Parameters
        ----------
        node_name
            Name of the node.

        node_label
            Name that will appear at the node.
        """
        if node_label is None:
            text = node_name
        else:
            text = node_label
        self.gr.node(node_name, self._str_key(text), shape="ellipse")

    @staticmethod
    def _str_key(label: str) -> str:
        """String processing for key attributes.

        Parameters
        ----------
        label
            Label to processed.

        Returns
        -------
        Processed label.
        """
        return f"<<u>{label}</u>>"

    def derived(self, node_name: str, node_label: Optional[str] = None):
        """This method declares a derived attribute.

        Parameters
        ----------
        node_name
            Name of the node.

        node_label
            Name that will appear at the node.
        """
        self.gr.node(
            node_name,
            process_label(node_label),
            shape="ellipse",
            style="dashed",
        )

    def weak_key(self, node_name: str, node_label: Optional[str] = None):
        """This method declares a weak key attribute.

        Parameters
        ----------
        node_name
            Name of the node.

        node_label
            Name that will appear at the node.
        """
        if node_label is None:
            text = node_name
        else:
            text = node_label
        self.gr.node(node_name, label=self._weak_key(text), shape="ellipse")

    @staticmethod
    def _weak_key(label: str) -> str:
        """String processing for weak key attributes.

        Parameters
        ----------
        label
            Label to processed.

        Returns
        -------
        Processed label.
        """
        return f"""<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="0">
    <TR>
        <TD COLSPAN="1" SIDES="B" STYLE="dashed">{label}</TD>
    </TR>
    </TABLE>>"""

    def relation(
        self,
        relation_name: str,
        attr1: str,
        attr2: str,
        label_attr1: Optional[str] = None,
        label_attr2: Optional[str] = None,
        identifying: str = "no",
    ):
        """This method declares the relationship between attributes.

        Parameters
        ----------
        relation_name
            Text that will appear at the node.
        attr1
            The first entity.
        attr2
            The second entity.
        label_attr1
            Text that will appear between the relationship diamond and the first entity.
        label_attr2
            Text that will appear between the relationship diamond and the second entity.
        identifying
            No: single lines. Yes: double lines.
        """
        if identifying == "no":
            lines = "1"
        else:
            lines = "2"
        self.gr.node(relation_name, shape="diamond", peripheries=lines)
        # e.edge('C-I', 'institute', label='1', len='1.00')
        self.gr.edge(attr1, relation_name, label=process_label(label_attr1))
        self.gr.edge(attr2, relation_name, label=process_label(label_attr2))


if __name__ == "__main__":
    gr = graphviz.Graph("ER", filename="erd", engine="dot", format="png")
    obj = ERD(gr)

    # node name and node label
    obj.entity("entity1", "entity 1")
    # the label is optional as it is in graphviz
    obj.attribute("attr")
    # new lines using the html notation
    obj.multivalue("multi", "multivalued<BR/>attribute")
    obj.key("key", "key attribute")
    obj.derived("derived")
    obj.weak_key("weak")

    obj.associative_entity("assoc", "associative<BR/>entity")

    obj.weak_entity("entity2", "weak entity 2")
    obj.relation("relationship", "entity1", "entity2", "(1,2)", "(2, 1)", "yes")

    obj.gr.edges(
        [
            ("entity1", "attr"),
            ("entity1", "multi"),
            ("entity1", "key"),
            ("entity1", "weak"),
            ("entity1", "derived"),
        ]
    )

    obj.gr.view()
