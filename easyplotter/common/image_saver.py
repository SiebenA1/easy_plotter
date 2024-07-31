# -*- coding: utf-8 -*-
from pathlib import Path
from easyplotter.common.logger import Logger


class ImageSaver:
    def __init__(self, output_dir: Path):
        # Initialize logger
        self.logger = Logger(__name__, "DEBUG", Path("logs"), True).singleton_logger

        self.output_dir = output_dir

    def save(self, figure, plot_id: str) -> None:
        """
        Save the plot to a file

        Parameters
        ----------
        figure : matplotlib.figure.Figure
            to save
        plot_id : str
            Unique identifier for the plot
        """
        output_file = self.output_dir / f"{plot_id}.png"
        figure.savefig(output_file)
        self.logger.info(f"Save the plot to {output_file}.")
