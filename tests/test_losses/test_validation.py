from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "libs"))

from losses.aggregation import PRECIP_8760_ERROR_MESSAGE, aggregate_hourly_precipitation_to_monthly


def test_precipitation_length_must_be_8760():
    with pytest.raises(ValueError) as exc_info:
        aggregate_hourly_precipitation_to_monthly([0.0] * 8759, unit="mm")

    assert str(exc_info.value) == PRECIP_8760_ERROR_MESSAGE


def test_aggregation_is_deterministic_for_same_input():
    hourly = [1.0] * 8760

    result_a = aggregate_hourly_precipitation_to_monthly(hourly, unit="in")
    result_b = aggregate_hourly_precipitation_to_monthly(hourly, unit="in")

    assert result_a == result_b
