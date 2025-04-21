import numpy as np
def activation_func(x):
    return 1 if x>=0 else 0

def predict_func(inputs, weight, bais):
    ws = np.dot(inputs, weight) + bais
    return activation_func(ws)

def train(X, y, lr=0.1, epochs=10):
    weight = np.zeros(X.shape[1])
    bias = 0
    for epoch in range(epochs):
        for i in range(len(X)):
            ypred = predict_func(X[i], weight, bias)
            error = y[i] - ypred
            weight += lr * error * X[i]
            bias += lr * error
    return weight, bias

X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
    ])

AND_y = np.array([0,0,0,1]) #desired output

and_w, and_b = train(X, AND_y)
for input_data in X:
    print(f"Inputs: {input_data} -> Output: {predict_func(input_data, and_w, and_b)}")

            
    