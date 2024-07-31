# -*- coding: utf-8 -*-
"""Main script of easyplotter"""
from easyplotter.module.plot_manager import PlotManager
from easyplotter.configuration.args_parser import args_parse


def main():
    args = args_parse()
    output_dir = args.output
    output_dir.mkdir(parents=True, exist_ok=True)
    plot_manager = PlotManager(args.config, output_dir)
    plot_manager.create_plots()


if __name__ == "__main__":
    main()
