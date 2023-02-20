import pytest
from ..src.wonderD149Data.data import helper as hp


def test_getGroupByCategories():
    categories = hp.getGroupByCategories()
    assert(isinstance(categories,set))