import torch
from .Solver import Solver


class SequenceClassificationSolver(Solver):

    def _transform_prediction_output(self, prediction):
        prediction_probabilities = torch.softmax(prediction, dim=1)
        _, predicted_classes = torch.max(prediction_probabilities, dim=1)
        return prediction, predicted_classes
