# Gradient Descent for Linear Regression
import numpy as np

# formula
# y = mx + b
# where,
#   m represents the slope and
#   b is the intercept on the y-axis.
# loss = (y - yhat)**2 / N

# Initialize parameters
x = np.random.randn(10, 1)
y = 2 * x + np.random.rand()

# Parameters
weights = 0.0
bias = 0.0

# Hyperparameter (also referred to as step size or the alpha)
learning_rate = 0.0


# Gradient descent function
def grad_desc(x, y, weights, bias, learning_rate):
    dldw = 0.0
    dldb = 0.0
    N = x.shape[0]

    # Loop through x and y value and calculate partial derivatives to update the weight and bias parameter
    for xi, yi in zip(x, y):
        dldw += -2 * xi * (yi - (weights * xi + bias))
        dldb += -2 * (yi - (weights * xi + bias))

    # Makinga an update to the weights parameter
    weights = weights - learning_rate * (1 / N) * dldw
    bias = bias - learning_rate * (1 / N) * dldb
    return weights, bias


# Iteratively make updates
for epochs in range(400):
    weights, bias = grad_desc(x, y, weights, bias, learning_rate)
    yhat = weights * x + bias
    loss = np.divide(np.sum((y - yhat)**2, axis=0), x.shape[0])
    print(f'{epochs} loss is {loss}, parameters weights: {weights}, bias: {bias}')
    # pass
