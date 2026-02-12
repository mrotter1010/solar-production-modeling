from .aggregation import (
    PRECIP_8760_ERROR_MESSAGE,
    aggregate_hourly_precipitation_to_monthly,
)
from .soiling import soiling_loss_from_monthly_precipitation
from .types import MonthlyPrecipitation, MonthlySoilingLoss, PrecipitationUnit

__all__ = [
    "PRECIP_8760_ERROR_MESSAGE",
    "PrecipitationUnit",
    "MonthlyPrecipitation",
    "MonthlySoilingLoss",
    "aggregate_hourly_precipitation_to_monthly",
    "soiling_loss_from_monthly_precipitation",
]
