from abc import abstractmethod

from typing_extensions import Protocol


# UnverifiedDuration should be used when accepting input from untrusted sources (pretty much anywhere) in the model.
# This type models input that has not been verified and is therefore unsafe to use until it has been verified.
# Use Verify() to transform it to trusted input in the form of a duration model.
from money.money import Money


class Duration(Protocol):

	@abstractmethod
	def DurationInMinutes(self) -> int:
		pass


class UnverifiedDuration:
	def __init__(self, durationInMinutes: int):
		self._durationInMinutes: int = durationInMinutes

	def Verify(self) -> Duration:
		return DurationInMinutes(self._durationInMinutes)



def DurationInMinutes(durationInMinutes: int) -> Duration:
	if durationInMinutes <= 0:
		raise ValueError("duration should be a positive number in minutes")

	return _duration(durationInMinutes=durationInMinutes)


class _duration(Duration):
	def __init__(self, durationInMinutes: int):
		self._durationInMinutes: int = durationInMinutes

	def DurationInMinutes(self) -> int:
		return self._durationInMinutes


def CalculateRidePrice(pricePerMinute: Money, duration: Duration) -> Money:
	return pricePerMinute.MultiplyAndRound(float(duration.DurationInMinutes()))
