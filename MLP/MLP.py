import numpy as np

class Dense:
    def __init__(self, n_inputs, n_neurons):
        self.W = np.random.rand(n_inputs, n_neurons)/100.0
        self.b = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.dot(self.inputs, self.W) + self.b

    def backward(self, dvalues):
        self.dW = np.dot(self.inputs.T, dvalues)
        self.db = np.sum(dvalues, axis=0, keepdims=True)

        self.dinputs= np.dot(dvalues, self.W.T)

class ActivationSigmoid:
    def forward(self, inputs):
        self.inputs = inputs
        self.output = 1/ (1+np.exp(-inputs))

    def backward(self, dvalues):
        self.dinputs = dvalues * (1-self.ouput) * self.output

    def predictions(self, outputs):
        return (outputs> 0.5) * 1

class ActivationSoftmax:
    def forward(self, inputs):
        self.inputs = inputs
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

class ActivationReLU:

    # Forward pass
    def forward(self, inputs):
        # Remember input values
        self.inputs = inputs
        # Calculate output values from inputs
        self.output = np.maximum(0, inputs)

    # Backward pass
    def backward(self, dvalues):
        # Since we need to modify original variable,
        # let's make a copy of values first
        self.dinputs = dvalues.copy()

        # Zero gradient where input values were negative
        self.dinputs[self.inputs <= 0] = 0


class CategoricalCrossEntropyLoss:


    def forward(self, y_pred, y_true):
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7) #prevent log(0)
        correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)

        # Losses
        CEntropy = -np.log(correct_confidences)
        return CEntropy 

    def backward(self, dvalues, y_true):
        samples = len(dvalues)

        y_true = np.argmax(y_true, axis=1)

        self.dinputs = dvalues.copy()
        # Calculate gradient
        self.dinputs[range(samples), y_true] -= 1
        # Normalize gradient
        self.dinputs = self.dinputs / samples

class Backpropagation:
    def __init__(self, lr):
        self.lr = lr

    def updateParams(self, layer):
        layer.W += -self.lr * layer.dW
        layer.b += -self.lr * layer.db
