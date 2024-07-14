import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, \
    classification_report
from sklearn.model_selection import cross_val_predict, cross_val_score, KFold


class ClassificationMetrics:
    def __init__(self, model, X, y, cv=100):
        self.model = model
        self.X = X
        self.y = y
        self.cv = cv
        self.kf = KFold(n_splits=cv, shuffle=True, random_state=42)

    def get_cross_val_metrics(self):
        accuracy = cross_val_score(self.model, self.X, self.y, cv=self.cv, scoring='accuracy')
        precision = cross_val_score(self.model, self.X, self.y, cv=self.cv, scoring='precision_weighted')
        recall = cross_val_score(self.model, self.X, self.y, cv=self.cv, scoring='recall_weighted')
        f1 = cross_val_score(self.model, self.X, self.y, cv=self.cv, scoring='f1_weighted')

        metrics = {
            'Fold': range(1, self.cv + 1),
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1 Score': f1
        }
        return pd.DataFrame(metrics)

    def get_confusion_matrix(self):
        y_pred = cross_val_predict(self.model, self.X, self.y, cv=self.cv)
        return pd.DataFrame(confusion_matrix(self.y, y_pred))

    def get_classification_report(self):
        y_pred = cross_val_predict(self.model, self.X, self.y, cv=self.cv)
        report_dict = classification_report(self.y, y_pred, output_dict=True)
        return pd.DataFrame(report_dict).transpose()