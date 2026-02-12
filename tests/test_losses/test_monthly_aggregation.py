from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "libs"))

from losses.aggregation import (
    INCHES_PER_MM,
    MONTH_LENGTHS_HOURS,
    aggregate_hourly_precipitation_to_monthly,
)


def test_monthly_aggregation_with_inches_input():
    hourly = [1.0] * 8760

    result = aggregate_hourly_precipitation_to_monthly(hourly, unit="in")

    expected = [float(hours) for hours in MONTH_LENGTHS_HOURS]
    assert result.inches == expected


def test_monthly_aggregation_with_millimeter_conversion():
    hourly_mm = [25.4] * 8760

    result = aggregate_hourly_precipitation_to_monthly(hourly_mm, unit="mm")

    expected = [float(hours) for hours in MONTH_LENGTHS_HOURS]
    assert result.inches == pytest.approx(expected)


def test_mm_to_inches_conversion_constant():
    assert 25.4 * INCHES_PER_MM == pytest.approx(1.0)
