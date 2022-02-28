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

    def test_weak_key(self):
        answer = """<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="0">
    <TR>
        <TD COLSPAN="1" SIDES="B" STYLE="dashed">a</TD>
    </TR>
    </TABLE>>"""
        calculated = ERD._weak_key("a")
        print(calculated)
        self.assertEqual(calculated, answer)


if __name__ == "__main__":
    unittest.main()
