# -*- coding: utf-8 -*-
from pathlib import Path
import argparse


def args_parse():
    """
    Parse the arguments
    """
    parser = argparse.ArgumentParser(description="Create pictures from the test results")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("easyplotter/configuration/config.json"),
        help="The path to the configuration file"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("test_results"),
        help="The path to the output file"
    )
    return parser.parse_args()
