import pandas as pd
import numpy as np
import config
import os
from scipy.stats import ttest_ind, chi2_contingency
from statsmodels.stats.weightstats import DescrStatsW


class DataLoader:

    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None

    def load_data(self):
        
        if os.path.exists(self.data_path):
            self.df = pd.read_csv(self.data_path)

            return self.df
        
        else:
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        

    def filter_years(self, years):
        if self.df is not None:
            return self.df[self.df["year"].isin(years)].copy()
        else:
            raise ValueError("Data not loaded. Please load the data first.")
        


