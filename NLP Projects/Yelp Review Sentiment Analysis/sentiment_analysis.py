"""
3-layer neural network with ReLU activations for Yelp review sentiment classification
Loads pre-trained GloVe embeddings and converts reviews into averaged embedding vectors
Trains using mini-batch gradient descent with evaluation on train/dev splits
Includes a demo with 2D XOR dataset using logistic regression and a simple neural net
Utilities provided for dataset loading, embedding handling, and model validation

├── util.py
│   └── contains: load_embeddings, load_dataset, check_parameter_shapes, check_forward_pass, check_backward_pass, check_predict, check_examples_to_array, plotting helpers, evaluate()
├── data/
│   ├── glove.dataset_small.50d.txt    # pre-trained GloVe word embeddings
│   ├── train.csv                      # training set: text reviews + labels
│   └── dev.csv                        # dev/validation set: text reviews + labels
│
├── main.py
│   ├── Imports: numpy, os, typing, gensim, sklearn, and util functions
│   ├── Hyperparameters: LEARNING_RATE=0.1, NUM_EPOCHS=50, BATCH_SIZE=5000
│   ├── 2D XOR demo: generates toy dataset, trains logistic regression + neural net
│   ├── StackedLogisticRegressionNetwork: basic 3-layer network with sigmoid activations
│   ├── YelpClassificationNeuralNetwork: extends above, uses ReLU + better weight init
│   ├── Loads GloVe embeddings & Yelp reviews datasets
│   ├── Converts text reviews into averaged embedding vectors
│   ├── Trains Yelp sentiment classifier with mini-batch gradient descent
│   └── Predicts sentiment on sample reviews

Imports for math, data structures, typing, embeddings, OS utils, and custom utilities
"""

import numpy as np
np.random.seed(1)
from util import *
import os
from typing import Dict, List, Tuple
import gensim.models
import sys
# %matplotlib inline -> displays matplotlib plots

"""
Hyperparameters used for training:
- Learning Rate: 0.1
- Number of Epochs: 50
- Batch Size: 5000
"""

print("Generating and plotting 2D XOR dataset...")
X, y = generate_2d_xor_dataset()
plot_2d_dataset_points(X, y)

from sklearn.linear_model import LogisticRegression
print("Training Logistic Regression classifier on XOR dataset...")
logistic_regression_classifier = LogisticRegression().fit(X, np.squeeze(y))
print("Plotting Logistic Regression predictions...")
plot_points_with_classifier_predictions(X, y, logistic_regression_classifier)

# Initialize weights and biases for each layer of the network
class StackedLogisticRegressionNetwork:
    def __init__(self, input_size: int, layer_1_size: int, layer_2_size: int, seed: int = 1):
        np.random.seed(seed)
        self.W_1 = self.initialize_weights(input_size, layer_1_size)
        self.b_1 = np.zeros((1, layer_1_size))
        self.W_2 = self.initialize_weights(layer_1_size, layer_2_size)
        self.b_2 = np.zeros((1, layer_2_size))
        self.W_3 = self.initialize_weights(layer_2_size, 1)
        self.b_3 = np.zeros((1, 1))
        self.variables = {
            "W_1": self.W_1,
            "b_1": self.b_1,
            "W_2": self.W_2,
            "b_2": self.b_2,
            "W_3": self.W_3,
            "b_3": self.b_3
        }

    # Initialize weights using uniform distribution based on layer sizes
    @staticmethod
    def initialize_weights(num_inputs: int, num_outputs: int) -> np.ndarray:
        bound = np.sqrt(6 /(num_inputs + num_outputs))
        return np.random.uniform(-bound, bound, (num_inputs, num_outputs))

    # Sigmoid activation function
    @staticmethod
    def sigmoid(z: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-z))

    # Perform forward propagation through the network layers
    def forward_pass(self, X: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        z1 = X @ self.W_1 + self.b_1
        a_1 = self.sigmoid(z1)
        z2 = a_1 @ self.W_2 + self.b_2
        a_2 = self.sigmoid(z2)
        z3 = a_2 @ self.W_3 + self.b_3
        a_3 = self.sigmoid(z3)
        return a_1, a_2, a_3

    # Compute gradients via backpropagation for all parameters
    def backward_pass(self, X: np.ndarray, y: np.ndarray, a_1: np.ndarray, a_2: np.ndarray, a_3: np.ndarray) -> Dict[str, np.ndarray]:
        m = X.shape[0]
        dz3 = a_3 - y
        dW3 = (a_2.T @ dz3) / m
        db3 = np.sum(dz3, axis=0, keepdims=True) / m
        da2 = dz3 @ self.W_3.T
        dz2 = da2 * a_2 * (1 - a_2)
        dW2 = (a_1.T @ dz2) / m
        db2 = np.sum(dz2, axis=0, keepdims=True) / m
        da1 = dz2 @ self.W_2.T
        dz1 = da1 * a_1 * (1 - a_1)
        dW1 = (X.T @ dz1) / m
        db1 = np.sum(dz1, axis=0, keepdims=True) / m
        gradients = {
            "W_1": dW1,
            "b_1": db1,
            "W_2": dW2,
            "b_2": db2,
            "W_3": dW3,
            "b_3": db3
        }
        return gradients

    # Update weights and biases with computed gradients
    def update_parameters(self, gradients: Dict[str, np.ndarray], learning_rate: float):
        for key in self.variables:
            self.variables[key] -= learning_rate * gradients[key]

    # Train the model using the full dataset for a number of epochs
    def train(self, X: np.ndarray, y: np.ndarray, learning_rate: float, num_epochs: int, print_every: int = 1000):
        for epoch in range(num_epochs):
            a_1, a_2, a_3 = self.forward_pass(X)
            gradients = self.backward_pass(X, y, a_1, a_2, a_3)
            self.update_parameters(gradients, learning_rate)
            if (epoch + 1) % print_every == 0:
                loss = -np.mean(y * np.log(a_3 + 1e-8) + (1 - y) * np.log(1 - a_3 + 1e-8))
                print(f"Epoch {epoch+1}, Loss: {loss:.4f}")

    # Predict binary labels based on output probabilities
    def predict(self, X: np.ndarray) -> np.ndarray:
        _, _, a_3 = self.forward_pass(X)
        return (a_3 >= 0.5).astype(int)

print("Checking model parameters and forward/backward passes...")
check_parameter_shapes(StackedLogisticRegressionNetwork)
check_forward_pass(StackedLogisticRegressionNetwork, X)
check_backward_pass(StackedLogisticRegressionNetwork, X, y)
check_predict(StackedLogisticRegressionNetwork, X)

print("Training Stacked Logistic Regression Neural Network...")
neural_network_classifier = StackedLogisticRegressionNetwork(2, 10, 10)
neural_network_classifier.train(X, y, learning_rate=0.1, num_epochs=10000, print_every=1000)

print("Plotting points with neural network classifier predictions...")
plot_points_with_classifier_predictions(X, y, neural_network_classifier)

print("Loading embeddings from GloVe dataset...")
embeddings = load_embeddings("data/glove.dataset_small.50d.txt")

words = ['terrible', 'good', 'nice']
print("\nSample word embeddings:")
for word in words:
    print(f"{word} : {embeddings[word]}")
print(f"<unk> embedding : {embeddings['<unk>']}")
print(f"Is 'nice' in embeddings? { 'nice' in embeddings }")
print(f"Is 'EasterEgg' in embeddings? { 'EasterEgg!' in embeddings }")

print("\nLoading training and development datasets...")
train_examples, train_labels = load_dataset("data/train.csv")
dev_examples, dev_labels = load_dataset("data/dev.csv")

EXAMPLES_TO_PRINT = 5
print(f"\nPrinting first {EXAMPLES_TO_PRINT} training examples and labels:")
for text, label in zip(train_examples[:EXAMPLES_TO_PRINT], train_labels[:EXAMPLES_TO_PRINT]):
    print(f"Review: {' '.join(text)}")
    print(f"Sentiment: {label}\n")

# Aggregate a list of word embeddings into a single vector by a specified mode
def aggregate_embeddings(list_of_embeddings: List[np.ndarray], mode: str="mean") -> np.ndarray:
    if not list_of_embeddings:
        return np.zeros((50,))
    array = np.array(list_of_embeddings)
    if mode == "mean":
        aggregated = np.mean(array, axis=0)
    elif mode == "sum":
        aggregated = np.sum(array, axis=0)
    elif mode == "max":
        aggregated = np.amax(array, axis=0)
    else:
        raise ValueError("Invalid mode: {}".format(mode))
    return aggregated

# Convert list of text examples to arrays of aggregated embeddings
def examples_to_array(examples: List[List[str]], embeddings: gensim.models.KeyedVectors, mode: str="mean"):
    if not examples:
        return np.zeros((0, 50))
    examples_list = []
    for example in examples:
        list_of_embeddings = []
        for word in example:
            if word in embeddings:
                list_of_embeddings.append(embeddings[word])
            else:
                list_of_embeddings.append(embeddings['unk'])
        aggregate = aggregate_embeddings(list_of_embeddings, mode)
        examples_list.append(aggregate)
    examples_array = np.array(examples_list)
    return examples_array

print("Checking examples_to_array function with embeddings...")
check_examples_to_array(examples_to_array, embeddings)

print("Converting training and development examples to arrays...")
train_examples_array = examples_to_array(train_examples, embeddings)
train_labels_array = np.expand_dims(np.array(train_labels), axis=1)
dev_examples_array = examples_to_array(dev_examples, embeddings)
dev_labels_array = np.expand_dims(np.array(dev_labels), axis=1)

class YelpClassificationNeuralNetwork(StackedLogisticRegressionNetwork):
    # Extend base network with ReLU activations and modified initialization for Yelp sentiment task
    def __init__(self, *args, **kwargs):
        super(YelpClassificationNeuralNetwork, self).__init__(*args, **kwargs)

    # Initialize weights using normal distribution with adjusted stddev
    @staticmethod
    def initialize_weights(num_inputs: int, num_outputs: int) -> np.ndarray:
        stddev = np.sqrt(2 /(num_inputs + num_outputs))
        return np.random.normal(0, stddev, (num_inputs, num_outputs))

    # ReLU activation function
    @staticmethod
    def relu(x: np.ndarray) -> np.ndarray:
        return np.maximum(0, x)

    # Forward pass using ReLU in hidden layers and sigmoid in output
    def forward_pass(self, X: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        z1 = X @ self.W_1 + self.b_1
        a_1 = self.relu(z1)
        z2 = a_1 @ self.W_2 + self.b_2
        a_2 = self.relu(z2)
        z3 = a_2 @ self.W_3 + self.b_3
        a_3 = self.sigmoid(z3)
        return a_1, a_2, a_3

    # Backpropagation with ReLU derivatives
    def backward_pass(self, X: np.ndarray, y: np.ndarray, a_1: np.ndarray, a_2: np.ndarray, a_3: np.ndarray) -> Dict[str, np.ndarray]:
        m = X.shape[0]
        dz3 = a_3 - y
        dW3 = (a_2.T @ dz3) / m
        db3 = np.sum(dz3, axis=0, keepdims=True) / m
        da2 = dz3 @ self.W_3.T
        dz2 = da2 * (a_2 > 0).astype(float)
        dW2 = (a_1.T @ dz2) / m
        db2 = np.sum(dz2, axis=0, keepdims=True) / m
        da1 = dz2 @ self.W_2.T
        dz1 = da1 * (a_1 > 0).astype(float)
        dW1 = (X.T @ dz1) / m
        db1 = np.sum(dz1, axis=0, keepdims=True) / m
        gradients = {
            "W_1": dW1,
            "b_1": db1,
            "W_2": dW2,
            "b_2": db2,
            "W_3": dW3,
            "b_3": db3
        }
        return gradients

    # Update weights and biases with gradients during batch training
    def update_parameters(self, gradients: Dict[str, np.ndarray], learning_rate: float):
        for key in self.variables:
            self.variables[key] -= learning_rate * gradients[key]

    # Train model using mini-batches with shuffling, and evaluate on dev set periodically
    def train_batch(self, X_train: np.ndarray, y_train: np.ndarray, X_dev: np.ndarray, y_dev: np.ndarray,
                    learning_rate: float, batch_size: int, num_epochs: int, print_every: int = 10):
        m = X_train.shape[0]
        for epoch in range(num_epochs):
            permutation = np.random.permutation(m)
            X_train_shuffled = X_train[permutation]
            y_train_shuffled = y_train[permutation]
            for i in range(0, m, batch_size):
                X_batch = X_train_shuffled[i:i+batch_size]
                y_batch = y_train_shuffled[i:i+batch_size]
                a_1, a_2, a_3 = self.forward_pass(X_batch)
                gradients = self.backward_pass(X_batch, y_batch, a_1, a_2, a_3)
                self.update_parameters(gradients, learning_rate)
            if (epoch + 1) % print_every == 0:
                a_1_dev, a_2_dev, a_3_dev = self.forward_pass(X_dev)
                loss = -np.mean(y_dev * np.log(a_3_dev + 1e-8) + (1 - y_dev) * np.log(1 - a_3_dev + 1e-8))
                preds = (a_3_dev >= 0.5).astype(int)
                accuracy = np.mean(preds == y_dev)
                print(f"Epoch {epoch+1}, Dev Loss: {loss:.4f}, Dev Acc: {accuracy:.4f}")

"""
in util.py:
def evaluate(model, examples_to_array, embeddings, text: str):
    tokens = text.lower().split()
    x = examples_to_array([tokens], embeddings)
    pred = model.predict(x)[0][0]
    sentiment = "Positive" if pred == 1 else "Negative"
    print(f"Review: {text}")
    print(f"Predicted Sentiment: {sentiment}\n")
"""

print("Training YelpClassificationNeuralNetwork model...")
model = YelpClassificationNeuralNetwork(50, 100, 100)
model.train_batch(
    train_examples_array,
    train_labels_array,
    dev_examples_array,
    dev_labels_array,
    learning_rate=0.1,
    batch_size=5000,
    num_epochs=50,
    print_every=10
)

print("\nFinal Predictions:")
evaluate(model, examples_to_array, embeddings, "I did not like it.")
evaluate(model, examples_to_array, embeddings, "The food was fantastic.")
