# -*- coding: utf-8 -*-
from pathlib import Path

from easyplotter.common.data_provider import DataProvider
from easyplotter.common.image_saver import ImageSaver
from easyplotter.common.plot_builder import PlotBuilder
from easyplotter.module.plotting import PlotSettings, PlotSignals, PlotVerticalLines, PlotAnnotation
from easyplotter.configuration.config_parser import ConfigParser
from easyplotter.common.logger import logger


class PlotManager:
    """
    Manager for creating plots
    """

    def __init__(self, config_path: Path, output_dir: Path):
        """
        Initialize plot manager with a configuration file path

        Parameters
        ----------
        config_path : Path
            Path to the configuration file
        """
        logger.info("Initialize PlotManager.")
        # Initialize ImageSaver
        self.image_saver = ImageSaver(output_dir)
        # Initialize configuration parser
        self.config_parser = ConfigParser(config_path)
        # Get time domain plots configuration
        self.plots_configs = self.config_parser.get_time_domain_plots()

    def create_plots(self) -> None:
        """
        Create plots based on the configuration
        """
        for plots_config in self.plots_configs:
            dataset = DataProvider()
            time, data = dataset.load_data(data_path=Path('tests/data/filtered_signal_segment.csv'))

            # Create a plot builder
            builder = PlotBuilder()
            logger.info("Create a PlotBuilder.")

            # Apply plotter to the builder to build a coordinate system
            PlotSettings(plots_config['plot_settings']).apply(builder)
            logger.info("Apply PlotCoordSys to the PlotBuilder.")

            # Apply plotter to the builder to add signals
            PlotSignals(time, data, plots_config['signals']).apply(builder)
            logger.info("Apply PlotSignals to the PlotBuilder.")

            # Apply plotter to the builder to add vertical lines
            PlotVerticalLines(plots_config['vertical_lines']).apply(builder)
            logger.info("Apply PlotVerticalLines to the PlotBuilder.")

            # Apply general settings to the plot
            PlotAnnotation(plots_config['id'], plots_config['description']).apply(builder)
            logger.info("Apply PlotGeneral to the PlotBuilder.")

            # Save the plot
            self.image_saver.save(builder.figure, plots_config['id'])
            logger.info("Save the plot.")

            builder.show()
            logger.info("Show the plot.")
