# %%
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, \
    classification_report
from sklearn.model_selection import cross_val_score


# %%
class ClassificationMetrics:
    def __init__(self, model, Y_test, Y_prediction, cv=10):
        self.cv = cv
        self.model = model
        self.Y_test = Y_test
        self.Y_prediction = Y_prediction

    def get_score(self):

        metrics = {
            'Accuracy': accuracy_score(self.Y_test, self.Y_prediction),
            'Precision': precision_score(self.Y_test, self.Y_prediction, average='weighted'),
            'Recall': recall_score(self.Y_test, self.Y_prediction, average='weighted'),
            'F1 Score': f1_score(self.Y_test, self.Y_prediction, average='weighted')
        }
        return pd.DataFrame([metrics])

    def get_confusion_matrix(self):
        return pd.DataFrame(confusion_matrix(self.Y_test, self.Y_prediction))

    def get_classification_report(self):
        report_dict = classification_report(self.Y_test, self.Y_prediction, output_dict=True)
        return pd.DataFrame(report_dict).transpose()
