from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "libs"))

from losses.soiling import soiling_loss_from_monthly_precipitation


def test_soiling_bin_boundaries_are_exact():
    monthly_inches = [2.0, 1.99, 1.5, 1.49, 1.0, 0.99, 0.5, 0.49, 0.0, 2.5, 1.2, 0.2]

    result = soiling_loss_from_monthly_precipitation(monthly_inches)

    assert result.percent == [1.0, 1.5, 1.5, 2.0, 2.0, 2.5, 2.5, 3.0, 3.0, 1.0, 2.0, 3.0]


def test_soiling_output_always_12_values_for_12_input_values():
    result = soiling_loss_from_monthly_precipitation([0.6] * 12)
    assert len(result.percent) == 12


def test_soiling_raises_for_negative_monthly_precipitation():
    with pytest.raises(ValueError, match="monthly precipitation values must be non-negative"):
        soiling_loss_from_monthly_precipitation([0.1] * 11 + [-0.01])
