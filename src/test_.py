import pytest
import unittest
import contactrx
import inputfunctions

# Test for contact lens prescription conversion
def test_clrx(monkeypatch):
    inputs = iter(['-9.50', '12'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert contactrx.clrx() == -8.50  

def test_clrx(monkeypatch):
    inputs = iter(['6.25', '13'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert contactrx.clrx() == +6.75

# Test to ensure the correct sentence is printed to terminal
class TestSpam(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_y_or_n(self):
        inputfunctions.y_or_n()
        captured = self.capsys.readouterr()
        self.assertEqual("Please enter 'Y' or 'N'.\n", captured.out)