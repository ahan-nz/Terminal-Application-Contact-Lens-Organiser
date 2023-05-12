# import pytest
import contactrx

def test_clrx(monkeypatch):
    inputs = iter(['-9.50', '12'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert contactrx.clrx() == -8.50  
