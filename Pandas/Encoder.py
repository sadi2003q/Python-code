from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder
from sklearn.impute import KNNImputer
from sklearn.compose import ColumnTransformer


class Encoder:
    def __init__(self, x, y,
                 label_code=False,
                 ordinal_code=None,
                 category=None,
                 onehot_code=None,
                 missing_value=None,
                 scale_value=None):

        if ordinal_code is None:
            ordinal_code = []
        if onehot_code is None:
            onehot_code = []
        if category is None:
            category = []
        if missing_value is None:
            missing_value = []
        if scale_value is None:
            scale_value = []

        self.label_code = label_code
        self.ordinal_code = ordinal_code
        self.onehot_code = onehot_code
        self.category = category
        self.missing_Value = missing_value
        self.scale_value = scale_value
        self.x = x
        self.y = y

    def encode(self):
        self.transform()
        if self.label_code:
            self.label_transform()

        return self.x, self.y

    def transform(self):
        transformer = ColumnTransformer(transformers=[
            ('missing Value', KNNImputer(n_neighbors=10, weights='distance'), self.missing_Value),
            ('ordinal', OrdinalEncoder(), self.ordinal_code),
            ('onehot', OneHotEncoder(drop='first', sparse_output=False), self.onehot_code)
        ], remainder='passthrough')
        self.x = transformer.fit_transform(self.x)

    def label_transform(self):
        label_encoder = LabelEncoder()
        self.y = label_encoder.fit_transform(self.y)
