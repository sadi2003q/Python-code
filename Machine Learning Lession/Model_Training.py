from sklearn.model_selection import train_test_split as split
from Machine_Learning.Classification_Regressor import Regression
from Machine_Learning.Classification_Logistic import ClassificationMetrics


class Model_Training:
    def __init__(self, model, data, target, is_Regression=True):
        self.reg = is_Regression
        self.prediction = None
        self.model = model
        self.x = data
        self.y = target
        self.train_x = None
        self.train_y = None
        self.test_x = None
        self.test_y = None

    def Splitting(self):
        self.train_x, self.test_x, self.train_y, self.test_y = split(self.x, self.y, test_size=0.2)
        self.model.fit(self.train_x, self.train_y)
        self.prediction = self.model.predict(self.test_x)

    def run(self):
        self.Splitting()
        if self.reg:
            return Regression(self.model, self.train_x, self.train_y,  self.test_y, self.prediction)
        else:
            return ClassificationMetrics(self.model, self.train_x, self.train_y, self.test_y, self.prediction)
