[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![github-actions](https://github.com/mashi/codecov-validator/actions/workflows/ci.yml/badge.svg)](https://github.com/mashi/graphviz-erd/actions)
[![codecov](https://codecov.io/gh/mashi/graphviz-erd/branch/main/graph/badge.svg?token=MR7OATF18B)](https://codecov.io/gh/mashi/graphviz-erd)
[![Documentation Status](https://readthedocs.org/projects/graphviz-erd/badge/?version=latest)](https://graphviz-erd.readthedocs.io/en/latest/?badge=latest)

# graphviz-erd

Draw Entity Relationship Diagrams (ERD) with python and graphviz.

This code is built on top of the [graphviz](https://pypi.org/project/graphviz/) python package and provides methods to facilitate the declaration of blocks commonly used in ERD such as entities and attributes.


## Example

We can draw diagrams like
![erd](https://media.githubusercontent.com/media/mashi/graphviz-erd/main/fig/erd.png)
<!--
Link to the image because it was not showing in pypi.org.
To obtain the link:
1. Go to the image address in the Github repository.
2. right click on the image and select 'Copy Image Link'
-->

using the code:
```
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

    # draw relation between entities
    obj.relation("relationship", "entity1", "entity2", "(1,2)", "(2, 1)", "yes")

    # connect the attributes
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
```


## Instructions (Development)

The code was developed inside a virtual environment using git hooks. To facilitate the process,
assuming a linux environment (Ubuntu), some recipes with makefile are available.

To install all the dependencies and to configure the git hooks:
```
make install
```

To build the documentation locally calling sphinx:
```
make docs
```
To access the generated documentation, open the file `docs/_build/index.html'.

To execute tests:
```
make tests
```

To build the python package:
```
make build
```
