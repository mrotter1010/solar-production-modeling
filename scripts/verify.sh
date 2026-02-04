#!/usr/bin/env bash
set -euo pipefail

tmp_dir=$(mktemp -d)
outputs_root="$tmp_dir/outputs"

python run.py --input tests/data/sample_sites.csv --outputs-root "$outputs_root" --log-level INFO

run_dir=$(ls -1 "$outputs_root/_runs" | sort | tail -n 1)
run_inputs="$outputs_root/_runs/$run_dir/run_inputs_${run_dir}.json"

if [[ ! -f "$run_inputs" ]]; then
  echo "Missing run inputs file: $run_inputs" >&2
  exit 1
fi

customer_dir="$outputs_root/Acme_Energy"
site_dir="$customer_dir/Desert_Site/$run_dir"
if [[ ! -d "$site_dir" ]]; then
  echo "Missing site output directory: $site_dir" >&2
  exit 1
fi

inputs_file="$site_dir/Desert_Site_Run_A_${run_dir}_inputs.json"
if [[ ! -f "$inputs_file" ]]; then
  echo "Missing site inputs file: $inputs_file" >&2
  exit 1
fi

invalid_site_dir="$customer_dir/unknown/$run_dir"
error_file="$invalid_site_dir/unknown_Run_B_${run_dir}_error.json"
if [[ ! -f "$error_file" ]]; then
  echo "Missing error file: $error_file" >&2
  exit 1
fi

pytest -q
