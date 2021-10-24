import pytest

from money import Money


def test_money_equals_detects_equal_values():
	assert Money.EUR(99)==(Money.EUR(99))


def test_money_equals_detects_currency_differences():
	assert Money.EUR(10) != (Money.USD(10))


def test_money_equals_detects_amount_differences():
	assert Money.EUR(1) != Money.EUR(2)


def test_money_multiply_multiplies():
	assert Money.EUR(200).MultiplyAndRound(2.00) == Money.EUR(400)


def test_money_multiply_rounds_upward_correctly():
	assert Money.EUR(100).MultiplyAndRound(1.999) == Money.EUR(200)


def test_money_multiply_rounds_downward_correctly():
	assert Money.EUR(100).MultiplyAndRound(1.994) == Money.EUR(199)


@pytest.mark.skip(reason="Todo")
def test_money_amount_exposes_value():
	pass


@pytest.mark.skip(reason="Todo")
def test_money_currencyIsoCode_exposes_value():
	pass