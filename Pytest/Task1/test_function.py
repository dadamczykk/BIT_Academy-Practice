from function import square
# Napisać cztery testy z dla funckji square dla 0, 1, -1 i 100
def test_one():
    assert square(0) == 0
def test_two():
    assert square(1) == 1
def test_tree():
    assert square(-1) == 1
def test_four():
    assert square(100) == 100 ** 2