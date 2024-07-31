# -*- coding: utf-8 -*-
import json
from pathlib import Path

from easyplotter.common.logger import logger


class ConfigParser:
    """
    Configuration parser for reading configuration files
    """
    def __init__(self, config_path: Path) -> None:
        """
        Initialize configuration parser with a configuration file path

        Parameters
        ----------
        config_path : Path
            Path to the configuration file

        """
        # Initialize logger
        logger.info("Initialize ConfigParser.")

        with open(config_path, 'r') as file:
            self.config = json.load(file)

    def get_time_domain_plots(self) -> dict:
        """
        Get time domain plots configuration from the configuration file

        Returns
        -------
        dict
            Time domain plots configuration
        """
        logger.info("Get time domain plots configuration.")
        return self.config.get('visualization', {}).get('time_domain_plot', [])
