from __future__ import annotations

import csv
from pathlib import Path

from climate.types import AssembledClimate


FIELDNAMES = [
    "Year",
    "Month",
    "Day",
    "Hour",
    "Minute",
    "GHI",
    "DNI",
    "DHI",
    "Tdry",
    "Wspd",
    "RHum",
    "Pres",
]


def write_sam_csv(climate: AssembledClimate, output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["Latitude", "Longitude", "Time zone", "Elevation"])
        writer.writerow(
            [
                f"{climate.site.latitude:.6f}",
                f"{climate.site.longitude:.6f}",
                str(climate.site.timezone),
                f"{climate.site.elevation:.2f}",
            ]
        )
        dict_writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        dict_writer.writeheader()
        for row in climate.rows:
            dict_writer.writerow(row)
    return path
