from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


PrecipitationUnit = Literal["in", "mm", "m"]


@dataclass(frozen=True)
class MonthlyPrecipitation:
    inches: list[float]


@dataclass(frozen=True)
class MonthlySoilingLoss:
    percent: list[float]
