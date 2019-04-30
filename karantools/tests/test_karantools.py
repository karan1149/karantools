import karantools as kt
import pytest

def test_average_simple():
	assert(kt.average([1, 2, 3]) == 2)
	assert(kt.average([1]) == 1)
	assert(kt.average([1, 2, 3, 4]) == 2.5)

	with pytest.raises(ZeroDivisionError):
		kt.average([])

def test_average_or_0():
	assert(kt.average_or_0([1, 2, 3]) == 2)
	assert(kt.average_or_0([1]) == 1)
	assert(kt.average_or_0([1, 2, 3, 4]) == 2.5)

	assert(kt.average_or_0([]) == 0)

def test_average_streamer():
	streamer = kt.AverageStreamer()

	0, 1, 3, 6, 10, 15, 21
	averages = [0, 0.5, 1, 1.5, 2, 2.5, 3]

	with pytest.raises(ZeroDivisionError):
		streamer.query()

	for i in range(7):
		streamer.add(i)
		assert(streamer.query() == averages[i])

def test_assert_and_print():
	kt.assert_and_print(1, 1 > 0)
	kt.assert_and_print(1, 1 >= 0)
	kt.assert_and_print(1, 1 >= 1)
	test_list = [1, 2, 3]
	kt.assert_and_print(test_list, kt.average(test_list) == 2)

	with pytest.raises(AssertionError):
		test_list = [1, 2, 3]
		kt.assert_and_print(test_list, kt.average(test_list) == 3)

def test_assert_eq():
	with pytest.raises(AssertionError):
		kt.assert_eq(1, 2)

	with pytest.raises(AssertionError):
		kt.assert_eq(1, [])

	with pytest.raises(AssertionError):
		kt.assert_eq(0, [])

	kt.assert_eq(1, 1)

def test_assert_float_eq():
	with pytest.raises(AssertionError):
		kt.assert_float_eq(1, 2)

	with pytest.raises(AssertionError):
		kt.assert_float_eq(1, 1 + 1e-3)

	kt.assert_float_eq(1, 1 + 1e-10)

def test_assert_neq():
	kt.assert_neq(1, 2)

	kt.assert_neq(1, [])

	kt.assert_neq(0, [])

	with pytest.raises(AssertionError):
		kt.assert_neq(1, 1)

def test_assert_float_neq():
	kt.assert_float_neq(1, 2)

	kt.assert_float_neq(1, 1 + 1e-3)

	with pytest.raises(AssertionError):
		kt.assert_float_neq(1, 1 + 1e-10)
