import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score


class Regression:
    def __init__(self, model, test_y, prediction, cv=100):
        self.cv = cv
        self.model = model
        self.test_y = test_y
        self.prediction = prediction

    def get_score(self):
        r2 = r2_score(self.test_y, self.prediction)
        mean_square = mean_squared_error(self.test_y, self.prediction)
        mean_absolute = mean_absolute_error(self.test_y, self.prediction)

        metrics = {
            "r2_score": r2,
            "mean_absolute_error": mean_square,
            "mean_squared_error": mean_absolute,
        }

        return pd.DataFrame([metrics])  # Return as a DataFrame with one row
