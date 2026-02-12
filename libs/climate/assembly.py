from __future__ import annotations

from climate.index import build_hourly_index
from climate.types import AssembledClimate, SiteInfo
from climate.validation import validate_8760, validate_monthly_albedo, validate_required_non_null


def _round(value: float | None) -> float | None:
    return None if value is None else round(float(value), 3)


def assemble_site_climate(
    site: SiteInfo,
    nsrdb_hourly: dict,
    era_hourly: dict,
    metar_hourly: dict,
    monthly_albedo: list[float],
) -> AssembledClimate:
    idx = build_hourly_index(site.year)
    monthly_albedo = validate_monthly_albedo(monthly_albedo)

    rows: list[dict[str, float | int]] = []
    coverage = {"era": 0, "metar": 0, "missing": 0}

    for ts in idx:
        key = ts.isoformat()
        solar = nsrdb_hourly.get(key, {})
        era = era_hourly.get(key, {})
        metar = metar_hourly.get(key, {})

        temperature = era.get("temperature")
        source = "era"
        if temperature is None:
            temperature = metar.get("temperature")
            source = "metar" if temperature is not None else "missing"
        coverage[source] += 1

        row = {
            "Year": ts.year,
            "Month": ts.month,
            "Day": ts.day,
            "Hour": ts.hour,
            "Minute": 0,
            "GHI": _round(solar.get("ghi")),
            "DNI": _round(solar.get("dni")),
            "DHI": _round(solar.get("dhi")),
            "Tdry": _round(temperature),
            "Wspd": _round(era.get("wind_speed")),
            "RHum": _round(era.get("relative_humidity")),
            "Pres": _round(era.get("pressure")),
        }
        rows.append(row)

    validate_8760(rows)
    if coverage["missing"]:
        raise ValueError("Temperature fallback failed for one or more hours")
    validate_required_non_null(rows)

    return AssembledClimate(site=site, rows=rows, monthly_albedo=monthly_albedo, temperature_coverage=coverage)
