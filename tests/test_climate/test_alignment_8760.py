from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "libs"))

import pytest

from climate.assembly import assemble_site_climate
from climate.index import build_hourly_index
from climate.types import SiteInfo


def _full_era(year: int) -> dict:
    return {
        ts.isoformat(): {
            "temperature": 22.0,
            "wind_speed": 1.0,
            "relative_humidity": 40.0,
            "pressure": 1010.0,
        }
        for ts in build_hourly_index(year)
    }


def _full_nsrdb(year: int) -> dict:
    return {
        ts.isoformat(): {"ghi": 100.0, "dni": 50.0, "dhi": 30.0}
        for ts in build_hourly_index(year)
    }


def test_build_index_is_8760_and_no_feb_29():
    idx = build_hourly_index(2024)
    assert len(idx) == 8760
    assert all(not (ts.month == 2 and ts.day == 29) for ts in idx)


def test_assembly_fails_when_temperature_missing_after_fallback():
    site = SiteInfo("site-a", 35.0, -115.0, 500.0, -8, 2023)
    idx = build_hourly_index(2023)
    era = _full_era(2023)
    era[idx[10].isoformat()]["temperature"] = None
    metar = {}

    with pytest.raises(ValueError, match="Temperature fallback failed"):
        assemble_site_climate(site, _full_nsrdb(2023), era, metar, [0.2] * 12)
