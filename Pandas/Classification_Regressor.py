import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score


class Regression:
    def __init__(self, model, train_x, train_y, test_y, prediction, cv=10):
        self.cv = cv
        self.model = model
        self.test_y = test_y
        self.train_x = train_x
        self.train_y = train_y
        self.prediction = prediction

    def get_score(self):
        r2 = r2_score(self.test_y, self.prediction)
        mean_square = mean_squared_error(self.test_y, self.prediction)
        mean_absolute = mean_absolute_error(self.test_y, self.prediction)

        metrics = {
            "r2_score": r2,
            "mean_absolute_error": mean_square,
            "mean_squared_error": mean_absolute,
            "cross_val_score": cross_val_score(self, self.train_x, self.train_y, cv=self.cv, scoring='accuracy')
        }

        return pd.DataFrame([metrics])

    def ind_r2_score(self):
        return r2_score(self.test_y, self.prediction)

    def ind_mean_absolute_error(self):
        return mean_absolute_error(self.test_y, self.prediction)

    def ind_mean_squared_error(self):
        return mean_squared_error(self.test_y, self.prediction)