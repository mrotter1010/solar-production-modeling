from __future__ import annotations

from .types import MonthlySoilingLoss


def soiling_loss_from_monthly_precipitation(monthly_inches: list[float]) -> MonthlySoilingLoss:
    if len(monthly_inches) != 12:
        raise ValueError(f"monthly precipitation must contain exactly 12 values; received {len(monthly_inches)}")

    losses: list[float] = []
    for value in monthly_inches:
        if value < 0:
            raise ValueError("monthly precipitation values must be non-negative")
        if value >= 2.0:
            losses.append(1.0)
        elif value >= 1.5:
            losses.append(1.5)
        elif value >= 1.0:
            losses.append(2.0)
        elif value >= 0.5:
            losses.append(2.5)
        else:
            losses.append(3.0)

    return MonthlySoilingLoss(percent=losses)
