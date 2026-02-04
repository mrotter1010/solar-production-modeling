from __future__ import annotations

import argparse
import logging
import sys

from solar_production_modeling.runner import run_batch


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Solar production batch runner")
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--outputs-root", default="outputs", help="Outputs root directory")
    parser.add_argument("--fail-fast", action="store_true", help="Stop on first row error")
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging verbosity",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    logging.basicConfig(level=getattr(logging, args.log_level))
    logger = logging.getLogger("solar_production_modeling")

    try:
        result = run_batch(
            input_csv=args.input,
            outputs_root=args.outputs_root,
            fail_fast=args.fail_fast,
            logger=logger,
        )
    except Exception as exc:
        logger.error("Failed to run batch: %s", exc)
        return 1

    if result.success_count == 0:
        logger.error("All rows failed")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
