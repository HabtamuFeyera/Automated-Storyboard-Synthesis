import unittest
from evaluation_metrics import compute_accuracy

class TestEvaluationMetrics(unittest.TestCase):
    def test_compute_accuracy(self):
        y_true = [0, 1, 1, 0, 1]
        y_pred = [0, 1, 0, 0, 1]
        self.assertAlmostEqual(compute_accuracy(y_true, y_pred), 0.8, places=2)

if __name__ == "__main__":
    unittest.main()
