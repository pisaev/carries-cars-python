from pytest import raises

from money.money import Money
import pricing_engine


def test_calculate_price_charged_per_minute():
	pricePerMinute = Money.EUR(30)

	duration = pricing_engine.DurationInMinutes(2)

	assert pricing_engine.CalculatePrice(pricePerMinute, duration) == Money.EUR(60)


def test_duration_guards_against_zero_or_negative_duration():
	with raises(expected_exception=ValueError,match="duration should be a positive number in minutes"):
		pricing_engine.DurationInMinutes(0)


def test_UnverifiedDuration_valid_input():
	inMinutes = 1
	unverifiedInput = pricing_engine.UnverifiedDuration(durationInMinutes=inMinutes)
	verifiedInput = unverifiedInput.Verify().DurationInMinutes()

	assert pricing_engine.DurationInMinutes(inMinutes).DurationInMinutes() == verifiedInput


def test_UnverifiedDuration_invalid_input():
	inMinutes = 0
	unverifiedInput = pricing_engine.UnverifiedDuration(durationInMinutes=inMinutes)

	with raises(expected_exception=ValueError, match="duration should be a positive number in minutes"):
		unverifiedInput.Verify()
