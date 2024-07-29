import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, \
    classification_report
from sklearn.model_selection import cross_val_score


class ClassificationMetrics:
    def __init__(self, model, train_x, train_y, Y_test, Y_prediction, cv=10):
        self.cv = cv
        self.model = model
        self.Y_test = Y_test
        self.Y_prediction = Y_prediction
        self.train_x = train_x
        self.train_y = train_y

    def get_score(self):
        metrics = {
            'Accuracy': accuracy_score(self.Y_test, self.Y_prediction),
            'Precision': precision_score(self.Y_test, self.Y_prediction, average='weighted'),
            'Recall': recall_score(self.Y_test, self.Y_prediction, average='weighted'),
            'F1 Score': f1_score(self.Y_test, self.Y_prediction, average='weighted'),
            'Cross Val Score': np.mean(cross_val_score(self.model, self.train_x, self.train_y, cv=self.cv,
                                                       scoring='accuracy'))
        }
        return pd.DataFrame([metrics])

    def get_confusion_matrix(self):
        return pd.DataFrame(confusion_matrix(self.Y_test, self.Y_prediction))

    def get_classification_report(self):
        report_dict = classification_report(self.Y_test, self.Y_prediction, output_dict=True)
        return pd.DataFrame(report_dict).transpose()

    def ind_Accuracy_score(self):
        return accuracy_score(self.Y_test, self.Y_prediction)

    def ind_Precision_score(self):
        return precision_score(self.Y_test, self.Y_prediction)

    def ind_Recall_score(self):
        return recall_score(self.Y_test, self.Y_prediction)