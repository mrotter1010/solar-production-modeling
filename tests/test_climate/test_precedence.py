from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "libs"))

from climate.assembly import assemble_site_climate
from climate.index import build_hourly_index
from climate.types import SiteInfo


def _base_solar(year: int) -> dict:
    return {
        ts.isoformat(): {"ghi": float(ts.hour), "dni": float(ts.hour), "dhi": float(ts.hour)}
        for ts in build_hourly_index(year)
    }


def test_temperature_precedence_era_then_metar():
    site = SiteInfo("site-a", 35.0, -115.0, 500.0, -8, 2023)
    index = build_hourly_index(2023)

    nsrdb = _base_solar(2023)
    era = {
        ts.isoformat(): {
            "temperature": None if i == 1 else 25.0,
            "wind_speed": 2.0,
            "relative_humidity": 35.0,
            "pressure": 1012.0,
        }
        for i, ts in enumerate(index)
    }
    metar = {index[1].isoformat(): {"temperature": 18.0}}

    result = assemble_site_climate(site, nsrdb, era, metar, [0.2] * 12)

    assert result.rows[0]["Tdry"] == 25.0
    assert result.rows[1]["Tdry"] == 18.0
    assert result.temperature_coverage["era"] == 8759
    assert result.temperature_coverage["metar"] == 1
    assert result.temperature_coverage["missing"] == 0
