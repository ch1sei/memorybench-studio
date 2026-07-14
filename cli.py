"""Command-line entry point for a local benchmark preview."""

import argparse
from schemas.models import BenchmarkCase
from benchmark.runners.runner import BenchmarkRunner
from reports.renderer import to_markdown


def main(argv=None):
    parser = argparse.ArgumentParser(prog="memorybench")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args(argv)
    cases = [BenchmarkCase("MB-CLI-001", "Preference recall", "recall", "brief")]
    run = BenchmarkRunner(lambda expected, observed: 1.0 if expected == observed else 0.0).run("local-preview", "synthetic", "default", cases, {"MB-CLI-001": "brief"})
    print(to_markdown(run) if args.format == "markdown" else run.to_dict())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
