"""
Logistic Regression classifier on text data using unigram bag-of-words features
Includes optional stopword removal and gradient descent training with batch updates
Evaluates performance on train and dev sets from the triage dataset

├── util.py
└── data/
    └── triage/
        ├── train.csv
        └── dev.csv
util.py -> load_data, Classifier, Example, evaluate, remove_stop_words
train.csv, dev.csv -> training set and testing/validation set respectively

Imports for data structures, typing, math, plotting, text feature extraction, and utilities
"""

from collections import defaultdict
import operator
import random
from typing import List, Dict, Union

import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

from util import load_data, Classifier, Example, evaluate, remove_stop_words

# Load the dataset
dataset = load_data("./data/triage")

# Sigmoid function applied element-wise to input array x
def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))

# Plot sigmoid function for visualization
x = np.arange(-10, 10, 0.01)
y = sigmoid(x)
plt.plot(x, y, color='blue', lw=2)
plt.show()

# Compute the average logistic loss for predicted probabilities y_pred and true labels y_true
# Includes clipping to avoid log(0) errors
def logistic_loss(y_pred: np.ndarray, y_true: np.ndarray) -> float:
    
    epsilon = 1e-8
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

# Print logistic loss for a single prediction-true pair
def print_loss(y_pred, y_true):
    print("Predicted = {}, True = {} : Loss = {}".format(
          y_pred, y_true, logistic_loss(np.array([y_pred]), np.array([y_true]))))

# Test logistic loss with example values
print_loss(0.0, 1)
print_loss(0.1, 1)
print_loss(0.3, 1)
print_loss(0.5, 1)
print_loss(0.7, 1)
print_loss(0.9, 1)
print_loss(0.99, 1)
print_loss(0.999999, 1)
print_loss(1, 1)

# Perform batch gradient descent to learn logistic regression weights and bias
# Includes early stopping if loss improvement is less than epsilon
# Prints training progress every print_every iterations
def gradient_descent(X: np.ndarray,
                     Y: np.ndarray,
                     batch_size: int = 2000,
                     alpha: float = 0.5,
                     num_iterations: int = 1000,
                     print_every: int = 100,
                     epsilon: float = 1e-8) -> (np.ndarray, float):
    
    W = np.zeros((X.shape[1],))
    b = 0
    Y = np.array(Y)
    loss = 0
    for i in range(num_iterations):
        if batch_size >= X.shape[0]:
            X_batch = X
            Y_batch = Y
        else:
            batch_indices = np.random.randint(X.shape[0], size=batch_size)
            X_batch = X[batch_indices, :]
            Y_batch = Y[batch_indices]

        A = sigmoid(np.dot(X_batch, W) + b)
        m = X_batch.shape[0]
        dW = np.dot(X_batch.T, (A - Y_batch)) / m
        db = np.sum(A - Y_batch) / m
        W -= alpha * dW
        b -= alpha * db
        prev_loss = loss
        loss = logistic_loss(A, Y_batch)

        if abs(prev_loss - loss) < epsilon:
            break

        if (i+1) % print_every == 0:
            predictions = A.copy()
            predictions[predictions >= 0.5] = 1
            predictions[predictions < 0.5] = 0
            accuracy = np.mean(predictions == Y_batch)
            print(f"Iteration {i+1}/{num_iterations}: Batch Accuracy: {accuracy},  Batch Loss = {loss}")
    return W, b

# Logistic Regression classifier using bag-of-words unigram features
# Can optionally filter stop words during vectorization
class LogisticRegressionClassifier(Classifier):
    def __init__(self, filter_stop_words: bool = None, batch_size: int = 2000,
                 alpha: float = 0.5, num_iterations: int = 1000,
                 print_every: int = 100, epsilon: float = 1e-8):
        super().__init__(filter_stop_words if filter_stop_words is not None else False)
        stop_words = list(self.stop_words) if isinstance(self.stop_words, set) else self.stop_words
        self.vectorizer = CountVectorizer(min_df=20, stop_words=stop_words)
        self.batch_size = batch_size
        self.alpha = alpha
        self.num_iterations = num_iterations
        self.print_every = print_every
        self.epsilon = epsilon
        self.W = None
        self.b = None

# Train the logistic regression model on the provided training examples
    def train(self, examples: List[Example]) -> None:
        texts = [' '.join(example.words) for example in examples]
        labels = np.array([example.label for example in examples])
        X = self.vectorizer.fit_transform(texts).toarray()
        self.W, self.b = gradient_descent(X, labels,
                                          batch_size=self.batch_size,
                                          alpha=self.alpha,
                                          num_iterations=self.num_iterations,
                                          print_every=self.print_every,
                                          epsilon=self.epsilon)
        
# Predict binary labels (0 or 1) for the given examples
    def classify(self, examples: List[Example]) -> List[int]:
        texts = [' '.join(example.words) for example in examples]
        X = self.vectorizer.transform(texts).toarray()
        predictions = sigmoid(np.dot(X, self.W) + self.b)
        return (predictions >= 0.5).astype(int).tolist()

# Return the learned weights vector
    def get_weights(self) -> np.ndarray:
        return self.W

# Evaluate classifier without stopword removal
print("\nPerformance on Unigrams, no stopword removal:")
lr_classifier = LogisticRegressionClassifier(filter_stop_words=False)
evaluate(lr_classifier, dataset)

# Evaluate classifier with stopword removal
print("\nPerformance on Unigrams w/ stopword removal:")
lr_classifier_swr = LogisticRegressionClassifier(filter_stop_words=True)
evaluate(lr_classifier_swr, dataset)

"""
Performance on Unigrams, no stopword removal:
Accuracy (train): 0.7882733060914188
Accuracy (dev): 0.769529731830548

Performance on Unigrams w/ stopword removal:
Accuracy (train): 0.7772023187304
Accuracy (dev): 0.759813447337738
"""
