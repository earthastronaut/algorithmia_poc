from . import poc

def test_poc():
    assert poc.apply("Jane") == "hello Jane"
