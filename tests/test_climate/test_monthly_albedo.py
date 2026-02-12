from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "libs"))

import pytest

from climate.assembly import assemble_site_climate
from climate.index import build_hourly_index
from climate.types import SiteInfo
from climate.validation import validate_monthly_albedo


def _full_era(year: int) -> dict:
    return {
        ts.isoformat(): {
            "temperature": 20.0,
            "wind_speed": 2.0,
            "relative_humidity": 30.0,
            "pressure": 1015.0,
        }
        for ts in build_hourly_index(year)
    }


def _full_nsrdb(year: int) -> dict:
    return {
        ts.isoformat(): {"ghi": 100.0, "dni": 80.0, "dhi": 20.0}
        for ts in build_hourly_index(year)
    }


def test_monthly_albedo_must_be_12_values():
    with pytest.raises(ValueError, match="exactly 12"):
        validate_monthly_albedo([0.2] * 11)


def test_monthly_albedo_remains_monthly_and_maps_by_month_in_output():
    site = SiteInfo("site-a", 35.0, -115.0, 500.0, -8, 2023)
    albedo = [round(0.1 + i * 0.01, 2) for i in range(12)]
    result = assemble_site_climate(site, _full_nsrdb(2023), _full_era(2023), {}, albedo)
    assert result.monthly_albedo == albedo
