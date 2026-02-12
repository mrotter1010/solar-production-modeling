from __future__ import annotations

from .types import MonthlyPrecipitation, PrecipitationUnit

HOURS_IN_NON_LEAP_YEAR = 8760
INCHES_PER_MM = 1.0 / 25.4
INCHES_PER_METER = 39.37007874015748
MONTH_LENGTHS_HOURS = [
    31 * 24,
    28 * 24,
    31 * 24,
    30 * 24,
    31 * 24,
    30 * 24,
    31 * 24,
    31 * 24,
    30 * 24,
    31 * 24,
    30 * 24,
    31 * 24,
]

PRECIP_8760_ERROR_MESSAGE = (
    "Hourly precipitation must contain exactly 8760 values for one non-leap year. "
    "If this cannot be satisfied, default to 2% monthly losses ([2]*12), "
    "or attempt to pull precipitation data again."
)


def _validate_precip_length(hourly_precipitation: list[float]) -> None:
    if len(hourly_precipitation) != HOURS_IN_NON_LEAP_YEAR:
        raise ValueError(PRECIP_8760_ERROR_MESSAGE)


def _to_inches(hourly_precipitation: list[float], unit: PrecipitationUnit) -> list[float]:
    if unit == "in":
        return hourly_precipitation
    if unit == "mm":
        return [value * INCHES_PER_MM for value in hourly_precipitation]
    if unit == "m":
        return [value * INCHES_PER_METER for value in hourly_precipitation]
    raise ValueError(f"Unsupported precipitation unit: {unit}")


def aggregate_hourly_precipitation_to_monthly(
    hourly_precipitation: list[float],
    unit: PrecipitationUnit,
) -> MonthlyPrecipitation:
    _validate_precip_length(hourly_precipitation)
    hourly_inches = _to_inches(hourly_precipitation, unit)

    monthly_inches: list[float] = []
    start = 0
    for month_hours in MONTH_LENGTHS_HOURS:
        end = start + month_hours
        monthly_inches.append(sum(hourly_inches[start:end]))
        start = end

    return MonthlyPrecipitation(inches=monthly_inches)
