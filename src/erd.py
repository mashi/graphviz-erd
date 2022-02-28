from typing import Optional

import graphviz


class ERD:
    """
    Parameters
    ----------
    filename
        Name of the generated dot code and image file.
    engine
        Specify the dot engine used to generate the image.
    image_format
        The image extension.

    Attributes
    ----------
    gr
        Graphviz object.
    """

    def __init__(
        self,
        filename: str = "erd",
        engine: str = "dot",
        image_format: str = "png",
    ) -> None:
        print(format)
        self.gr = graphviz.Graph(
            "ER", filename=filename, engine=engine, format=image_format
        )

    @staticmethod
    def _process_label(text: Optional[str]) -> Optional[str]:
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

    def entity(self, node_name: str, node_label: Optional[str] = None):
        """This method declares an entity.

        Parameters
        ----------
        node_name
            Name of the node.

        node_label
            Name that will appear at the node.
        """
        self.gr.node(node_name, self._process_label(node_label), shape="box")

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
            self._process_label(node_label),
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

        self.gr.node(
            node_name, self._process_label(node_label), shape="Msquare"
        )

    def attribute(self, node_name: str, node_label: Optional[str] = None):
        """This method declares an attribute.

        Parameters
        ----------
        node_name
            Name of the node.

        node_label
            Name that will appear at the node.
        """
        self.gr.node(
            node_name, self._process_label(node_label), shape="ellipse"
        )

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
            self._process_label(node_label),
            shape="ellipse",
            peripheries="2",
        )

    @staticmethod
    def _check_node_label(
        node_name: str, node_label: Optional[str] = None
    ) -> str:
        """Returns the node_name if the node_label is None. Otherwise, the
        node_name will be used as the label for the graphviz node.

        Parameters
        ----------
        node_name
            Name of the node.
        Node label
            Name that will appear at the node.

        Returns
        -------
        str
            The string that will be used as label.
        """
        if node_label is None:
            text = node_name
        else:
            text = node_label
        return text

    def key(self, node_name: str, node_label: Optional[str] = None):
        """This method declares a key attribute.

        Parameters
        ----------
        node_name
            Name of the node.

        node_label
            Name that will appear at the node.
        """
        text = self._check_node_label(node_name, node_label)
        self.gr.node(node_name, self._str_key(text), shape="ellipse")

    @staticmethod
    def _str_key(label: str) -> str:
        """String processing for key attributes.

        Parameters
        ----------
        label
            Label to be processed.

        Returns
        -------
        str
            Processed label.
        """
        return f"<<u>{label}</u>>"

    def weak_key(self, node_name: str, node_label: Optional[str] = None):
        """This method declares a weak key attribute.

        Parameters
        ----------
        node_name
            Name of the node.

        node_label
            Name that will appear at the node.
        """
        text = self._check_node_label(node_name, node_label)
        self.gr.node(node_name, label=self._str_weak_key(text), shape="ellipse")

    @staticmethod
    def _str_weak_key(label: str) -> str:
        """String processing for weak key attributes.

        Parameters
        ----------
        label
            Label to be processed.

        Returns
        -------
        str
            Processed label.
        """
        return f"""<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="0">
    <TR>
        <TD COLSPAN="1" SIDES="B" STYLE="dashed">{label}</TD>
    </TR>
    </TABLE>>"""

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
            self._process_label(node_label),
            shape="ellipse",
            style="dashed",
        )

    def relation(
        self,
        relation_name: str,
        ent1: str,
        ent2: str,
        label_ent1: Optional[str] = None,
        label_ent2: Optional[str] = None,
        identifying: str = "no",
    ):
        """This method declares the relationship between attributes.

        Parameters
        ----------
        relation_name
            Text that will appear at the node.
        ent1
            The first entity.
        ent2
            The second entity.
        label_ent1
            Text that will appear between the relationship diamond and the first entity.
        label_ent2
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
        self.gr.edge(ent1, relation_name, label=self._process_label(label_ent1))
        self.gr.edge(ent2, relation_name, label=self._process_label(label_ent2))


if __name__ == "__main__":
    obj = ERD()

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
