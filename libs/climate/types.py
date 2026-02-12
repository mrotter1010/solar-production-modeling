from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional


@dataclass(frozen=True)
class SiteInfo:
    site_id: str
    latitude: float
    longitude: float
    elevation: float
    timezone: int
    year: int


@dataclass(frozen=True)
class ClimatePoint:
    timestamp: datetime
    ghi: Optional[float] = None
    dni: Optional[float] = None
    dhi: Optional[float] = None
    temperature: Optional[float] = None
    wind_speed: Optional[float] = None
    relative_humidity: Optional[float] = None
    pressure: Optional[float] = None


@dataclass(frozen=True)
class AssembledClimate:
    site: SiteInfo
    rows: List[Dict[str, float | int]]
    monthly_albedo: List[float]
    temperature_coverage: Dict[str, int]
