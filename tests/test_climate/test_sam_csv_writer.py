from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "libs"))

from climate.assembly import assemble_site_climate
from climate.index import build_hourly_index
from climate.sam_csv import write_sam_csv
from climate.types import SiteInfo


def _full_era(year: int) -> dict:
    return {
        ts.isoformat(): {
            "temperature": 21.0,
            "wind_speed": 1.5,
            "relative_humidity": 45.0,
            "pressure": 1009.0,
        }
        for ts in build_hourly_index(year)
    }


def _full_nsrdb(year: int) -> dict:
    return {
        ts.isoformat(): {"ghi": 120.0, "dni": 60.0, "dhi": 40.0}
        for ts in build_hourly_index(year)
    }


def test_sam_csv_writer_outputs_header_and_8760_rows(tmp_path: Path):
    site = SiteInfo("site-a", 35.123456, -115.654321, 650.12, -8, 2023)
    climate = assemble_site_climate(site, _full_nsrdb(2023), _full_era(2023), {}, [0.2] * 12)

    out = write_sam_csv(climate, tmp_path / "sam_weather.csv")
    lines = out.read_text(encoding="utf-8").splitlines()

    assert lines[0] == "Latitude,Longitude,Time zone,Elevation"
    assert lines[1] == "35.123456,-115.654321,-8,650.12"
    assert lines[2].startswith("Year,Month,Day,Hour,Minute,GHI,DNI,DHI,Tdry,Wspd,RHum,Pres")
    assert len(lines) == 8763
