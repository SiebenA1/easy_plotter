# -*- coding: utf-8 -*-
from abc import ABC

import numpy as np

from easyplotter.common.plot_builder import PlotBuilder
from easyplotter.common.logger import logger


class Plotter(ABC):
    """
    Abstract class (interface) for plotter
    """

    def __init__(self):
        pass

    def apply(self, builder: PlotBuilder) -> None:
        pass


class PlotSettings(Plotter):
    """
    Plotter for coordinate system
    """

    def __init__(self, plot_settings: dict):
        """
        Initialize plotter with coordinate system settings

        Parameters
        ----------
        plot_settings : dict
            Coordinate system settings
        """
        super().__init__()
        self.title = plot_settings.get('title', '')
        x_axis_settings = plot_settings.get('x_axis_settings', {})
        self.x_label = x_axis_settings.get('x_label', '')
        self.x_axis = x_axis_settings.get('x_axis', '')
        y_axis_settings = plot_settings.get('y_axis_settings', {})
        self.y_label = y_axis_settings.get('y_label', '')
        self.y_axis = y_axis_settings.get('y_axis', '')

        logger.info("Initialize a PlotSettings.")

    def apply(self, builder: PlotBuilder) -> None:
        """
        Apply plot settings to plotBuilder
        """
        (builder.set_title(self.title).set_x_label(self.x_label).set_y_label(self.y_label).set_x_axis(self.x_axis).
         set_y_axis(self.y_axis).set_grids(True, True))


class PlotSignals(Plotter):
    """
    Plotter for signals
    """

    def __init__(self, time: np.ndarray, data: dict[str, np.ndarray], signals: list):
        """
        Initialize plotter with signals

        Parameters
        ----------
        time : np.ndarray
            Time domain
        data : np.ndarray
            Data to plot
        signals : list[dict]
            List of signals to plot
        """
        super().__init__()
        self.time = time
        self.data = data
        self.signals = signals

        # Initialize lists to store signal configurations
        self.signal_names = []
        self.y_datas = []
        self.labels = []
        self.colors = []
        self.line_styles = []
        self.line_widths = []

        # Populate the lists with the data from signals
        for signal in signals:
            self.signal_names.append(signal.get('signal_name'))
            self.labels.append(
                signal.get('label', signal['signal_name']))  # Default to signal_name if label is not provided
            self.colors.append(signal.get('color', 'black'))  # Default to black if color is not provided
            self.line_styles.append(signal.get('style', '-'))  # Default to solid line if line_style is not provided
            self.line_widths.append(signal.get('width', 1))  # Default to line width 1 if line_width is not provided
            self.y_datas.append(data.get(signal['signal_name']))

    logger.info("Initialize a PlotSignals.")

    def apply(self, builder: PlotBuilder) -> None:
        """
        Apply signals to plot builder

        Parameters
        ----------
        builder : PlotBuilder
            Plot builder to apply signals
        """
        for y_data, label, color, style, width in zip(self.y_datas,
                                                      self.labels,
                                                      self.colors,
                                                      self.line_styles,
                                                      self.line_widths):
            if y_data is None:
                logger.warning(f"Signal {label} not found in data. Skipping.")
                continue
            logger.info(f"Adding signal {label}")
            builder.add_signal(self.time, y_data,
                               label=label,
                               color=color,
                               linestyle=style,
                               linewidth=width)


class PlotVerticalLines(Plotter):
    def __init__(self, v_lines: list):
        """
        Initialize plotter with vertical lines

        Parameters
        ----------
        v_lines : list[dict]
            List of vertical lines
        """
        super().__init__()
        # Initialize lists to store vertical line configurations
        self.x_positions = []
        self.colors = []
        self.line_styles = []
        self.line_widths = []
        self.legends = []
        self.texts = []

        # Populate the lists with the data from vertical lines
        for v_line in v_lines:
            x_position = self._parse_x_position(v_line['x_position'])
            self.x_positions.append(x_position)
            self.colors.append(v_line.get('color', 'black'))
            self.line_styles.append(v_line.get('style', '--'))
            self.line_widths.append(v_line.get('width', 1))
            self.legends.append(v_line.get('legend', None))

            # Collect text information if available
            if 'text' in v_line:
                text = v_line['text']
                y_position = self._parse_text_position(text['text_y_position'])
                self.texts.append({
                    'x_position': x_position,
                    'y_position': y_position,
                    'text_content': text['text_content'],
                    'vertical_alignment': text.get('y_alignment', 'bottom'),
                    'horizontal_alignment': text.get('x_alignment', 'left')
                })
            else:
                self.texts.append({})

        logger.info("Initialize a PlotVerticalLines.")

    def apply(self, builder: PlotBuilder) -> None:
        """
        Apply vertical lines to plot builder

        Parameters
        ----------
        builder : PlotBuilder
            Plot builder to apply vertical lines
        """
        for i, x_position in enumerate(self.x_positions):
            builder.add_vertical_line(x_position,
                                      label=self.legends[i],
                                      color=self.colors[i],
                                      linestyle=self.line_styles[i],
                                      linewidth=self.line_widths[i])

            if self.texts[i] is not None:
                text = self.texts[i]
                builder.add_text(text['x_position'],
                                 text['y_position'],
                                 text['text_content'],
                                 verticalalignment=text['vertical_alignment'],
                                 horizontalalignment=text['horizontal_alignment'])

    @staticmethod
    def _parse_x_position(x_position: str) -> float:
        """
        Parse x position from string

        Parameters
        ----------
        x_position : str
            X position as string

        Returns
        -------
        float
            X position as float

        """
        return float(x_position.split()[0])

    @staticmethod
    def _parse_text_position(text_position: str) -> float:
        """
        Parse text position from string

        Parameters
        ----------
        text_position : str
            Text position as string

        Returns
        -------
        float
            Text position as float
        """
        # TODO for future implementation with complex text positions like X != 0
        return float(text_position.split()[0])


class PlotAnnotation(Plotter):
    """
    Plotter for Annotation
    """
    def __init__(self, plot_id: str, description: str):
        """
        Initialize plotter for annotation

        Parameters
        ----------
        plot_id : str
            Plot ID
        description : str
            Plot description
        """
        super().__init__()
        self.id = plot_id
        self.description = description
        logger.info("Initialize a PlotGeneral.")

    def apply(self, builder: PlotBuilder) -> None:
        """
        Apply annotation plot to plot builder

        Parameters
        ----------
        builder : PlotBuilder
            Plot builder to apply general plot
        """
        logger.info(f"Apply general plot {self.id} with description: {self.description}")
        builder.add_annotation(self.id + ': ' + self.description)
        builder.show()
