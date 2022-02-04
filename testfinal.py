def my_before_swap():
    tuple1 = (11, 22)
    tuple2 = (99, 88)

    print("before swapping \n tuple1 :", tuple1, "\n tuple2 :", tuple2)

my_before_swap()

def my_after_swap():
    tuple1 = (11, 22)
    tuple2 = (99, 88)
    tuple1, tuple2 = tuple2, tuple1
    print("after swapping \n tuple1 :", tuple1, "\n tuple2 :",tuple2)

my_after_swap()

expect_val = my_before_swap()
actual_val = my_before_swap()

def test_b():
    assert expect_val == actual_val

expect_value = my_after_swap()
actual_value = my_after_swap()

def test_a():
    assert expect_value == actual_value
