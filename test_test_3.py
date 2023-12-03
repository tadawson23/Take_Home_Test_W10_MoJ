"""Unit tests for test_3.py file"""

import pytest
from test_3 import sum_current_time


def test_sum_current_time_returns_int():
    """Tests that sum_current_time returns an integer"""
    assert isinstance(sum_current_time("12:12:12"), int)


def test_sum_current_time_raises_error():
    """Tests that an error is raised if the input is not a string"""
    with pytest.raises(ValueError):
        sum_current_time(50)


def test_sum_current_time_returns_correct_value():
    """Tests that sum_current_time returns the correct sum"""
    assert sum_current_time("12:12:50") == 74


def test_sum_current_time_returns_correct_value_2():
    """Tests that sum_current_time returns the correct sum"""
    assert sum_current_time("01:12:09") == 22


def test_sum_current_time_returns_correct_value_3():
    """Tests that sum_current_time returns the correct sum"""
    assert sum_current_time("12:10:10") == 32
