from __future__ import annotations

from abc import abstractmethod
from enum import Enum, auto

from typing_extensions import Protocol


class CurrencyIsoCode(Enum):
	Euro = auto()
	UnitedStatesDollar = auto()


class Money(Protocol):

	# EUR acts as a named constructor function to create trustedMoney for the Euro currency.
	# Provide the amount in cents.
	@classmethod
	def EUR(cls, amount: int) -> TrustedMoney:
		return TrustedMoney(amount=amount, currencyIsoCode=CurrencyIsoCode.Euro)

	# USD acts as a named constructor function to create trustedMoney for the UnitedStatesDollar currency.
	# Provide the amount in cents.
	@classmethod
	def USD(cls, amount: int) -> TrustedMoney:
		return TrustedMoney(amount=amount, currencyIsoCode=CurrencyIsoCode.UnitedStatesDollar)

	# Amount is denoted in the lowest denominator of the corresponding currency.
	# E.g. amount is in whole cents for the Euro or UnitedStatesDollar
	@abstractmethod
	def amount(self) -> int:
		pass

	@abstractmethod
	def currencyIsoCode(self) -> CurrencyIsoCode:
		pass

	@abstractmethod
	def MultiplyAndRound(self, multiplier: float) -> TrustedMoney:
		pass


# trustedMoney is hidden from the API surface to ensure that this type is trustworthy because it can only be created
# through one of the named constructors (EUR() or USD()).
class TrustedMoney(Money):
	# _amount is denoted in the lowest denominator of the corresponding currency.
	# E.g. _amount is in whole cents for the Euro or UnitedStatesDollar
	def __init__(self, amount: int, currencyIsoCode: CurrencyIsoCode):
		self._amount:  int = amount
		self._currencyIsoCode: CurrencyIsoCode =  currencyIsoCode

	def __eq__(self, other: TrustedMoney) -> bool:
		return self._amount == other._amount and self._currencyIsoCode == other._currencyIsoCode

	@property
	def amount(self) -> int:
		return self._amount

	@property
	def currencyIsoCode(self) -> CurrencyIsoCode:
		return self._currencyIsoCode

	def MultiplyAndRound(self, multiplier: float) -> TrustedMoney:
		multipliedAmount = self._amount * multiplier
		multipliedAmountRounded = int(round(multipliedAmount))

		return TrustedMoney(amount=multipliedAmountRounded, currencyIsoCode=self._currencyIsoCode)
