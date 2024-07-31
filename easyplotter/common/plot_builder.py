# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
import matplotlib.colors as mcolors

from easyplotter.common.logger import logger


class PlotBuilder:
    def __init__(self):
        """
        Initialize plot builder with default settings
        """
        logger.info("Initialize PlotBuilder.")
        self.figure, self.ax = plt.subplots(figsize=(12, 6))

    def set_title(self, title: str) -> 'PlotBuilder':
        """
        Set title for the plot

        Parameters
        ----------
        title : str
            Title for the plot

        Returns
        -------
        PlotBuilder
            Plot builder with a title set
        """
        self.ax.set_title(title)
        logger.info(f"Set title: {title}")
        return self

    def set_x_axis(self, x_axis: str) -> 'PlotBuilder':
        """
        Set x-axis for the plot

        Parameters
        ----------
        x_axis : str
            X-axis for the plot

        Returns
        -------
        PlotBuilder
            Plot builder with an x-axis set
        """
        try:
            start, stop, interval = map(float, x_axis.split('::'))
            self.ax.set_xlim((start, stop))
        except ValueError as e:
            logger.error(f"Failed to set x-axis limits: {e}")
        return self

    def set_y_axis(self, y_axis: str) -> 'PlotBuilder':
        """
        Set y-axis for the plot

        Parameters
        ----------
        y_axis : str
            Y-axis for the plot

        Returns
        -------
        PlotBuilder
            Plot builder with a y-axis set
        """
        try:
            start, stop, interval = map(float, y_axis.split('::'))
            self.ax.set_ylim((start, stop))
        except ValueError as e:
            logger.error(f"Failed to set y-axis limits: {e}")
        return self

    def set_grids(self, x_grid: bool, y_grid: bool) -> 'PlotBuilder':
        """
        Set grids for the plot

        Parameters
        ----------
        x_grid : bool
            X-axis grid
        y_grid : bool
            Y-axis grid

        Returns
        -------
        PlotBuilder
            Plot builder with grids set
        """
        # set major and minor ticks
        self.ax.xaxis.set_major_locator(ticker.MultipleLocator(5))  # set major ticks every 2 units
        self.ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))  # set minor ticks every 0.5 units

        # set color and transparency for major grid lines
        self.ax.grid(True, which='major', color=mcolors.to_rgba('gray', alpha=0.4), linestyle='-')
        # set color and transparency for minor grid lines
        self.ax.grid(True, which='minor', color=mcolors.to_rgba('gray', alpha=0.2), linestyle=':')

        logger.info(f"Set grids: x={x_grid}, y={y_grid}")
        return self

    def set_x_label(self, x_label: str) -> 'PlotBuilder':
        """
        Set x-axis label for the plot

        Parameters
        ----------
        x_label : str
            X-axis label for the plot

        Returns
        -------
        PlotBuilder
            Plot builder with an x-axis label set
        """
        self.ax.set_xlabel(x_label)
        logger.info(f"Set x-axis label: {x_label}")
        return self

    def set_y_label(self, y_label: str) -> 'PlotBuilder':
        """
        Set y-axis label for the plot

        Parameters
        ----------
        y_label : str
            Y-axis label for the plot

        Returns
        -------
        PlotBuilder
            Plot builder with a y-axis label set
        """
        self.ax.set_ylabel(y_label)
        logger.info(f"Set y-axis label: {y_label}")
        return self

    def add_signal(self, x_data: np.ndarray, y_data: np.ndarray, **kwargs: dict[str, int]) -> 'PlotBuilder':
        """
        Add a signal to the plot

        Parameters
        ----------
        x_data : np.ndarray
            X-axis data
        y_data : np.ndarray
            Y-axis data
        kwargs : dict[str, int]
            Additional arguments for plotting the signal

        Returns
        -------
        PlotBuilder
            Plot builder with a signal
        """
        self.ax.plot(x_data, y_data, **kwargs)
        self.ax.legend(loc="upper right", fontsize="small")
        logger.info(f"Add signal with {len(x_data)} data points.")
        return self

    def add_vertical_line(self, x_position: float, **kwargs: dict) -> 'PlotBuilder':
        """
        Add a vertical line to the plot

        Parameters
        ----------
        x_position : float
            X-axis position for the vertical line
        kwargs : dict
            Additional arguments for plotting the vertical line

        Returns
        -------
        PlotBuilder
            Plot builder with a vertical line
        """
        self.ax.axvline(x=x_position, **kwargs)
        self.ax.legend(loc="upper right", fontsize="small")
        logger.info(f"Add a vertical line at {x_position}.")
        return self

    def add_text(self, x: float, y: float, text: str, **kwargs: dict) -> 'PlotBuilder':
        """
        Add a text to the plot

        Parameters
        ----------
        x : float
            X-axis position for the text
        y : float
            Y-axis position for the text
        text : str
            Text to add to the plot
        kwargs : dict
            Additional arguments for the text

        Returns
        -------
        PlotBuilder
            Plot builder with a text
        """
        self.ax.text(x, y, text, **kwargs)
        logger.info(f"Add text '{text}' at ({x}, {y}).")
        return self

    def add_annotation(self, text: str) -> 'PlotBuilder':
        """
        Add an annotation to the plot

        Parameters
        ----------
        x : float
            X-axis position for the annotation
        y : float
            Y-axis position for the annotation
        text : str
            Text to add to the plot

        Returns
        -------
        PlotBuilder
            Plot builder with an annotation
        """
        self.figure.text(0.5, 0.0, text, ha='center', va='bottom', fontsize=10)
        return self

    @staticmethod
    def show():
        """
        Show the plot
        """
        return plt.show()
