"""Climate source adapters."""

from climate.adapters.era5 import load_era_hourly_json
from climate.adapters.metar import load_metar_hourly_json
from climate.adapters.nsrdb import load_nsrdb_hourly_json

__all__ = [
    "load_era_hourly_json",
    "load_metar_hourly_json",
    "load_nsrdb_hourly_json",
]
