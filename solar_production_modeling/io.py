from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable


def read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    csv_path = Path(path)
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError("CSV is missing header row")
        fieldnames = [name.strip() for name in reader.fieldnames]
        if len(set(fieldnames)) != len(fieldnames):
            raise ValueError("CSV header has duplicate column names after trimming")
        rows: list[dict[str, str]] = []
        for row in reader:
            normalized = {key.strip(): (value if value is not None else "") for key, value in row.items()}
            rows.append(normalized)
        return rows


def write_json(path: str | Path, data: dict | list) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, sort_keys=True)
        handle.write("\n")


def ensure_directory(path: str | Path) -> Path:
    output_path = Path(path)
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def write_text(path: str | Path, lines: Iterable[str]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for line in lines:
            handle.write(f"{line}\n")
