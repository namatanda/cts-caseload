#!/usr/bin/env python

"""Tests for `cts-caseload` package."""

import pytest

from cts_caseload import example_function


@pytest.fixture
def response():
    return 1, 2


def test_example_function(response):
    assert example_function(*response) == 3
