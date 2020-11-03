""" Example custom model
"""
import sklearn.tree


class CustomDecisionTree(sklearn.tree.DecisionTreeClassifier):
    """ Light wrapper around a decision tree
    """

    def __init__(self, *args, **kwargs):
        self.features = kwargs.pop('features')
        super().__init__(*args, **kwargs)

    def fit(self, x_features, y):
        """ Fit
        """
        x = x_features[self.features]
        return super().fit(x, y)

    def predict(self, x_features):
        """ Fit
        """
        x = x_features[self.features]
        return super().predict(x)
