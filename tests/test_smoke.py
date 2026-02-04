from __future__ import annotations

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from solar_production_modeling import runner, util


def test_smoke(tmp_path: Path) -> None:
    sample_csv = Path("tests/data/sample_sites.csv")
    outputs_root = tmp_path / "outputs"

    result = runner.run_batch(sample_csv, outputs_root=outputs_root)

    run_datetime = result.run_datetime
    run_inputs_path = outputs_root / "_runs" / run_datetime / f"run_inputs_{run_datetime}.json"
    assert run_inputs_path.exists()

    customer = util.sanitize_segment("Acme Energy")
    site_valid = util.sanitize_segment("Desert Site")
    run_name = util.sanitize_segment("Run A")
    valid_site_dir = outputs_root / customer / site_valid / run_datetime
    assert valid_site_dir.exists()

    valid_inputs = valid_site_dir / f"{site_valid}_{run_name}_{run_datetime}_inputs.json"
    assert valid_inputs.exists()

    invalid_site = util.sanitize_segment("")
    invalid_run = util.sanitize_segment("Run B")
    invalid_site_dir = outputs_root / customer / invalid_site / run_datetime
    assert invalid_site_dir.exists()

    invalid_error = invalid_site_dir / f"{invalid_site}_{invalid_run}_{run_datetime}_error.json"
    assert invalid_error.exists()

    other_customer = util.sanitize_segment("Beta Power")
    other_site = util.sanitize_segment("Coastal Site")
    other_run = util.sanitize_segment("Run C")
    other_site_dir = outputs_root / other_customer / other_site / run_datetime
    assert other_site_dir.exists()

    other_inputs = other_site_dir / f"{other_site}_{other_run}_{run_datetime}_inputs.json"
    assert other_inputs.exists()

    assert result.success_count == 2
    assert result.error_count == 1
