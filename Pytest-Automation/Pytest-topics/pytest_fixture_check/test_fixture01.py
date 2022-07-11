import pytest


def test_divisible_by_5(input_total):
    assert input_total % 5 == 0


def test_divisible_by_10(input_total):
    assert input_total % 10 == 0


def test_divisible_by_15(input_total):
    assert input_total % 15 == 0


def test_divisible_by_20(input_total):
    assert input_total % 20 == 0
