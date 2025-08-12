import numpy as np

# Activation function (Sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Take user input for dataset
n_samples = int(input("Enter number of samples: "))
n_features = int(input("Enter number of features: "))
n_outputs = int(input("Enter number of output neurons: "))

# Input features
X = []
for i in range(n_samples):
    row = list(map(float, input(f"Enter feature values for sample {i+1} (space-separated): ").split()))
    X.append(row)
X = np.array(X)

# Input target outputs
y = []
for i in range(n_samples):
    row = list(map(float, input(f"Enter target output values for sample {i+1} (space-separated): ").split()))
    y.append(row)
y = np.array(y)

# Define network architecture
hidden_neurons = int(input("Enter number of hidden layer neurons: "))
epochs = int(input("Enter number of training epochs: "))
learning_rate = float(input("Enter learning rate: "))

# Initialize weights and biases
input_layer_neurons = n_features
output_layer_neurons = n_outputs

hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_neurons))
hidden_bias = np.random.uniform(size=(1, hidden_neurons))
output_weights = np.random.uniform(size=(hidden_neurons, output_layer_neurons))
output_bias = np.random.uniform(size=(1, output_layer_neurons))

# Training process (Feedforward + Backpropagation)
for epoch in range(epochs):
    # Feedforward
    hidden_layer_input = np.dot(X, hidden_weights) + hidden_bias
    hidden_layer_activation = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_activation, output_weights) + output_bias
    predicted_output = sigmoid(output_layer_input)

    # Backpropagation
    error = y - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_activation)

    # Update weights and biases
    output_weights += hidden_layer_activation.T.dot(d_predicted_output) * learning_rate
    output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    hidden_weights += X.T.dot(d_hidden_layer) * learning_rate
    hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

# Display results
print("\nFinal hidden weights:\n", hidden_weights)
print("Final hidden bias:\n", hidden_bias)
print("Final output weights:\n", output_weights)
print("Final output bias:\n", output_bias)
print("\nPredicted Output:\n", predicted_output)
