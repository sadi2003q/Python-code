import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, make_scorer
from sklearn.model_selection import cross_val_score, cross_val_predict, KFold


class Regression:
    def __init__(self, model, X, y, cv=100):
        self.model = model
        self.X = X
        self.y = y
        self.cv = cv
        self.kf = KFold(n_splits=cv, shuffle=True, random_state=42)

    def get_cross_val_metrics(self):
        r2_scorer = make_scorer(r2_score)
        mae_scorer = make_scorer(mean_absolute_error)
        mse_scorer = make_scorer(mean_squared_error)

        r2_scores = cross_val_score(self.model, self.X, self.y, cv=self.cv, scoring=r2_scorer)
        mae_scores = cross_val_score(self.model, self.X, self.y, cv=self.cv, scoring=mae_scorer)
        mse_scores = cross_val_score(self.model, self.X, self.y, cv=self.cv, scoring=mse_scorer)

        metrics = {
            'Fold': range(1, self.cv + 1),
            'R2 Score': r2_scores,
            'Mean Absolute Error': mae_scores,
            'Mean Squared Error': mse_scores
        }
        return pd.DataFrame(metrics)

    def get_cross_val_predictions(self):
        y_pred = cross_val_predict(self.model, self.X, self.y, cv=self.cv)
        return pd.DataFrame({'Actual': self.y, 'Predicted': y_pred})
