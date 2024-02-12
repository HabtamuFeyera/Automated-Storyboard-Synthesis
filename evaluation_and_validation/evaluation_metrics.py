import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def compute_accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)

def compute_precision(y_true, y_pred):
    return precision_score(y_true, y_pred)

def compute_recall(y_true, y_pred):
    return recall_score(y_true, y_pred)

def compute_f1_score(y_true, y_pred):
    return f1_score(y_true, y_pred)

if __name__ == "__main__":
    # Example usage
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 1])
    print("Accuracy:", compute_accuracy(y_true, y_pred))
    print("Precision:", compute_precision(y_true, y_pred))
    print("Recall:", compute_recall(y_true, y_pred))
    print("F1-score:", compute_f1_score(y_true, y_pred))
