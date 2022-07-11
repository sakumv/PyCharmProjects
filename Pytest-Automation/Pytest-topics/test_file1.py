import pytest


def test_sample():
    assert 5*2 > 12, "failed"

def test_sample_2():
    assert 5//2 == 2

def test_sample_3():
    with pytest.raises(AssertionError):
        assert (1/0)

def funct():
    raise ValueError("Error is raised")

def test_sample_4():
    with pytest.raises(Exception) as exc_info:
        #assert (1,2,3) == (2,3,4)
        funct()
    print(exc_info)
    assert str(exc_info) == "Assertion Error"