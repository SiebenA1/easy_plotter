# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


class DataProvider:
    """
    Data provider class (temporary) to load data from a CSV file
    """
    def __init__(self):
        self.time = np.array([])
        self.data = np.array([])

    def load_data(self, data_path: Path) -> tuple[Any, dict[str, Any]]:
        """
        Load data from a CSV file

        Parameters
        ----------
        data_path : Path
            Path to the CSV file

        Returns
        -------
        tuple
            containing time and data dictionary
        """
        # Read the CSV file into a DataFrame
        df = pd.read_csv(data_path)

        # Ensure the DataFrame has at least two columns
        if df.shape[1] < 2:
            raise ValueError("CSV file must contain at least two columns")

        # Extract the first column as timestamp and the second column as signal_data
        self.time = df.iloc[:, 0].values
        AWV_Warnung = df.iloc[:, 1].values

        # Create and return the dictionary with the required format
        self.data = {
            'AWV_Warnung': AWV_Warnung
        }

        return self.time, self.data
