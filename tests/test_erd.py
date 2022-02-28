import unittest

from src.erd import ERD


class TestErd(unittest.TestCase):
    def test_passing_test(self):
        self.assertEqual(1, 1)

    def test_process_label_none(self):
        answer = None
        calculated = ERD._process_label(None)
        self.assertEqual(calculated, answer)

    def test_process_label_str(self):
        answer = "<a>"
        calculated = ERD._process_label("a")
        self.assertEqual(calculated, answer)

    def test_str_key(self):
        answer = "<<u>a</u>>"
        calculated = ERD._str_key("a")
        self.assertEqual(calculated, answer)

    def test_str_weak_key(self):
        answer = """<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="0">
    <TR>
        <TD COLSPAN="1" SIDES="B" STYLE="dashed">a</TD>
    </TR>
    </TABLE>>"""
        calculated = ERD._str_weak_key("a")
        print(calculated)
        self.assertEqual(calculated, answer)

    def test_entity(self):
        obj = ERD()
        name = "entity1"
        obj.entity(name)
        calculated = obj.gr.source
        answer = f"{name} [shape=box]"
        self.assertIn(answer, calculated)

    def test_weak_entity(self):
        obj = ERD()
        name = "entity1"
        obj.weak_entity(name)
        calculated = obj.gr.source
        answer = f"{name} [peripheries=2 shape=box]"
        self.assertIn(answer, calculated)

    def test_associative_entity(self):
        obj = ERD()
        name = "entity1"
        obj.associative_entity(name)
        calculated = obj.gr.source
        answer = f"{name} [shape=Msquare]"
        self.assertIn(answer, calculated)

    def test_attirbute(self):
        obj = ERD()
        name = "attribute"
        obj.attribute(name)
        calculated = obj.gr.source
        answer = f"{name} [shape=ellipse]"
        self.assertIn(answer, calculated)

    def test_multivalue(self):
        obj = ERD()
        name = "multivalued"
        obj.multivalue(name)
        calculated = obj.gr.source
        answer = f"{name} [peripheries=2 shape=ellipse]"
        self.assertIn(answer, calculated)

    def test_key(self):
        obj = ERD()
        name = "key"
        obj.key(name)
        calculated = obj.gr.source
        answer_shape = "shape=ellipse"
        answer_label = ERD._str_key(name)
        self.assertIn(answer_shape, calculated)
        self.assertIn(answer_label, calculated)

    def test_weak_key(self):
        obj = ERD()
        name = "key"
        obj.weak_key(name)
        calculated = obj.gr.source
        answer_shape = "shape=ellipse"
        answer_label = ERD._str_weak_key(name)
        self.assertIn(answer_shape, calculated)
        self.assertIn(answer_label, calculated)

    def test_derived(self):
        obj = ERD()
        name = "key"
        obj.derived(name)
        calculated = obj.gr.source
        answer = "[shape=ellipse style=dashed]"
        self.assertIn(answer, calculated)

    def test_relation(self):
        obj = ERD()
        name = "relationship"
        obj.relation(name, "ent1", "ent2")
        calculated = obj.gr.source
        answer_shape = "shape=diamond"
        answer_connection1 = f"ent1 -- {name}"
        answer_connection2 = f"ent2 -- {name}"
        self.assertIn(answer_shape, calculated)
        self.assertIn(answer_connection1, calculated)
        self.assertIn(answer_connection2, calculated)


if __name__ == "__main__":
    unittest.main()
