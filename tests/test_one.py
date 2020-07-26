from one.module_one import my_first_var as v_1
from two.module_two import my_second_var as v_2


def test_module_one():
    assert v_1


def test_module_two():
    assert v_2 == 2
