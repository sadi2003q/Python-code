import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, make_scorer
from sklearn.model_selection import cross_val_score


class RegressionMetrics:
    def __init__(self, y_true, y_pred, model=None, X=None, y=None):
        self.y_true = np.array(y_true)
        self.y_pred = np.array(y_pred)
        self.model = model
        self.X = X
        self.y = y

    def mean_absolute_error(self):
        return mean_absolute_error(self.y_true, self.y_pred)

    def mean_squared_error(self):
        return mean_squared_error(self.y_true, self.y_pred)

    def root_mean_squared_error(self):
        return np.sqrt(self.mean_squared_error())

    def r2_score(self):
        return r2_score(self.y_true, self.y_pred)

    def adjusted_r2_score(self):
        n = len(self.y_true)
        p = self.X.shape[1] if self.X is not None else 0
        r2 = self.r2_score()
        return 1 - (1 - r2) * (n - 1) / (n - p - 1)

    def mean_absolute_percentage_error(self):
        return np.mean(np.abs((self.y_true - self.y_pred) / self.y_true)) * 100

    def cross_val_score(self, cv=10):
        if self.model is None or self.X is None or self.y is None:
            raise ValueError("Model, X, and y must be provided for cross-validation.")

        scores = cross_val_score(self.model, self.X, self.y, cv=cv, scoring=make_scorer(mean_squared_error))
        return scores

    def get_all_metrics(self):
        metrics = {
            "Mean Absolute Error (MAE)": self.mean_absolute_error(),
            "Mean Squared Error (MSE)": self.mean_squared_error(),
            "Root Mean Squared Error (RMSE)": self.root_mean_squared_error(),
            "R-squared (R²)": self.r2_score(),
            "Adjusted R-squared (Adj. R²)": self.adjusted_r2_score(),
            "Mean Absolute Percentage Error (MAPE)": self.mean_absolute_percentage_error()
        }

        if self.model is not None and self.X is not None and self.y is not None:
            metrics["Cross Validation Score (MSE)"] = self.cross_val_score().mean()

        return metrics