import pytest
from pytest import raises

from money.money import Money
import pricing_engine


def test_calculate_price_charged_per_minute():
	pricePerMinute = Money.EUR(30)

	duration = pricing_engine.DurationInMinutes(2)

	assert pricing_engine.CalculateRidePrice(pricePerMinute, duration) == Money.EUR(60)


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


def test_base_reservation_has_zero_cost():
	MAX_BASE_RESERVATION_DURATION = 20
	reservationDuration = MAX_BASE_RESERVATION_DURATION - 1
	extendedReservationPricePerMinute = Money.EUR(2)
	assert pricing_engine.CalculateReservationPrice(reservationDuration, extendedReservationPricePerMinute) == [Money.EUR(0),Money.EUR(0)]


def test_extended_reservation_add_additional_cost():
	#reservation = pricing_engine.ReservationPricingCofiguration()
	MAX_BASE_RESERVATION_DURATION = 20
	reservationDuration = MAX_BASE_RESERVATION_DURATION + 1
	extendedReservationPricePerMinute = Money.EUR(2)
	assert pricing_engine.CalculateReservationPrice(reservationDuration, extendedReservationPricePerMinute) == [Money.EUR(0),Money.EUR(2)]

def test_extended_reservation_add_additional_cost1():
	MAX_BASE_RESERVATION_DURATION = 20
	reservationDuration = MAX_BASE_RESERVATION_DURATION + 2
	extendedReservationPricePerMinute = Money.EUR(2)
	assert pricing_engine.CalculateReservationPrice(reservationDuration, extendedReservationPricePerMinute) == [Money.EUR(0),Money.EUR(4)]
