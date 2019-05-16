"""
Tests for geom_analysis.py
"""

import geom_analysis as ga
import pytest

def test_calculate_distance():
    coord1 = [0, 0, 2]
    coord2 = [0, 0, 0]

    observed = ga.calculate_distance(coord1, coord2)

    assert observed == 2

def test_bond_check():
    bond_distance_test=2.0

    observed2 = ga.bond_check(bond_distance_test)

    assert observed2 == False

def test_bond_check_error():
    bond_length = 'a'

    with pytest.raises(TypeError):
        observed = ga.bond_check(bond_length)


