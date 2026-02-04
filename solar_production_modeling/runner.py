from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from solar_production_modeling import io, util

REQUIRED_IDENTIFIERS = ["Customer", "Site Name", "Run Name"]


@dataclass
class RunResult:
    run_datetime: str
    output_root: Path
    run_inputs_path: Path
    success_count: int
    error_count: int


def _validate_required_columns(rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ValueError("CSV contains no data rows")
    available = set(rows[0].keys())
    missing = [col for col in REQUIRED_IDENTIFIERS if col not in available]
    if missing:
        raise ValueError(f"CSV missing required columns: {', '.join(missing)}")


def run_batch(
    input_csv: str | Path,
    outputs_root: str | Path = "outputs",
    fail_fast: bool = False,
    logger: logging.Logger | None = None,
) -> RunResult:
    log = logger or logging.getLogger(__name__)
    rows = io.read_csv_rows(input_csv)
    _validate_required_columns(rows)

    run_datetime = util.current_run_timestamp()
    output_root = Path(outputs_root)
    run_records: list[dict[str, str]] = []
    success_count = 0
    error_count = 0

    stop_processing = False

    for index, row in enumerate(rows, start=1):
        row_record = dict(row)
        row_record["__row_index"] = str(index)
        row_record["__status"] = "ok"

        customer = row.get("Customer", "")
        site_name = row.get("Site Name", "")
        run_name = row.get("Run Name", "")

        customer_segment = util.sanitize_segment(customer)
        site_segment = util.sanitize_segment(site_name)
        run_segment = util.sanitize_segment(run_name)

        site_dir = output_root / customer_segment / site_segment / run_datetime

        error_info: dict[str, str] | None = None
        try:
            io.ensure_directory(site_dir)

            input_filename = f"{site_segment}_{run_segment}_{run_datetime}_inputs.json"
            input_path = site_dir / input_filename
            io.write_json(input_path, row)

            missing_identifiers = [
                name for name in REQUIRED_IDENTIFIERS if not (row.get(name) or "").strip()
            ]
            if missing_identifiers:
                error_info = {
                    "error_type": "ValidationError",
                    "message": f"Missing required identifiers: {', '.join(missing_identifiers)}",
                }
        except Exception as exc:
            error_info = {
                "error_type": "UnexpectedError",
                "message": str(exc),
            }

        if error_info:
            error_count += 1
            row_record["__status"] = "error"
            row_record["__error_type"] = error_info["error_type"]
            row_record["__error_message"] = error_info["message"]

            error_payload = {
                "error_type": error_info["error_type"],
                "message": error_info["message"],
                "row_index": index,
                "identifiers": {
                    "Customer": customer,
                    "Site Name": site_name,
                    "Run Name": run_name,
                },
            }
            error_filename = f"{site_segment}_{run_segment}_{run_datetime}_error.json"
            error_path = site_dir / error_filename
            try:
                io.write_json(error_path, error_payload)
            except Exception as exc:
                log.error("Failed to write error file for row %s: %s", index, exc)

            log.error("Row %s failed: %s", index, error_info["message"])
            if fail_fast:
                stop_processing = True
        else:
            success_count += 1
            log.info("Row %s processed successfully", index)

        run_records.append(row_record)

        if stop_processing:
            break

    run_inputs_dir = output_root / "_runs" / run_datetime
    run_inputs_path = run_inputs_dir / f"run_inputs_{run_datetime}.json"
    io.write_json(
        run_inputs_path,
        {
            "run_datetime": run_datetime,
            "input_csv_path": str(Path(input_csv)),
            "rows": run_records,
        },
    )

    return RunResult(
        run_datetime=run_datetime,
        output_root=output_root,
        run_inputs_path=run_inputs_path,
        success_count=success_count,
        error_count=error_count,
    )
