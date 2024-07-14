import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, make_scorer
from sklearn.model_selection import cross_val_score


class Regression:
    def __init__(self, test_y, prediction):
        self.test_y = test_y
        self.prediction = prediction

    def Get_All_Score(self):
        r2 = r2_score(self.test_y, self.prediction)

        metrics = {
            "r2_score": r2,
            "mean_absolute_error": mean_absolute_error(self.test_y, self.prediction),
            "mean_squared_error": mean_squared_error(self.test_y, self.prediction)
        }

        return pd.DataFrame([metrics])  # Return as a DataFrame with one row
