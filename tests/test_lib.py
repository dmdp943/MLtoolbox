# tests/test_lib.py
from MLtoolbox.lib import try_me

def test_try_me():
    assert type(try_me()) == str