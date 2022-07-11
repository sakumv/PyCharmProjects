import pytest

def test_divisible_by_3(input_total):
    assert input_total % 3 == 0


def test_divisible_by_6(input_total):
    assert input_total % 6 == 0


def test_divisible_by_9(input_total):
    assert input_total % 9 == 0
