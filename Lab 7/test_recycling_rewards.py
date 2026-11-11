
import pytest
from hypothesis import given, strategies as st
from recycling_rewards import (
    parse_collection,
    weight_average,
    net_points
)


# Test 1: parse_collection
@given(st.one_of(
    st.none(),
    st.text().filter(lambda s: s.count(":") != 1)
))
def test_parse_collection_invalid_format(s):
    with pytest.raises(ValueError):
        parse_collection(s)


@given(st.floats(max_value=-0.001,
                 allow_nan=False,
                 allow_infinity=False))
def test_parse_collection_negative_weight(weight):
    with pytest.raises(ValueError):
        parse_collection(f"paper:{weight}")


# Test 2: weight_average
@given(st.sampled_from([
    None, "", "1,,2", "abc", "1.5,2", ",",
    "-1,2", "1,2,"
]))
def test_weight_average_invalid_input(s):
    with pytest.raises(ValueError):
        weight_average(s)


# Test 3: net_points
@given(st.sampled_from([
    None, "", "80", "80|10|5",
    "abc|10", "80|abc", "-10|5", "80|-5"
]))
def test_net_points_invalid_input(s):
    with pytest.raises(ValueError):
        net_points(s)
