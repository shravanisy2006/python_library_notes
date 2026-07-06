# Tensorflow - Beginner Notes

## What is Tensorflow?

TensorFlow is a free, open-source software library developed by the Google Brain team for machine learning (ML) and artificial intelligence (AI). It provides a comprehensive ecosystem of tools, libraries, and community resources that allow developers and researchers to easily build, train, and deploy advanced ML models, particularly deep neural networks.

---

## Installing Tensorflow

pip install tensorflow

---

## Importing Tensorflow

import tensorflow as tf

---

**Key Features**
- Build Deep Learning models
- Automatic differentiation (Backpropagation)
- GPU/TPU acceleration
- Model deployment (Web, Mobile, Cloud)
- High-level API using Keras

---

# What is a Tensor?

A Tensor is the fundamental data structure in TensorFlow. It is a multi-dimensional array used to store and process data.

| Tensor Type | Rank | Example |
|-------------|------|---------|
| Scalar | 0 | 5 |
| Vector | 1 | [1,2,3] |
| Matrix | 2 | [[1,2],[3,4]] |
| 3D Tensor | 3 | Image Batch |
| 4D Tensor | 4 | Video/Data Batch |

Example:

```python
import tensorflow as tf

scalar = tf.constant(10)
vector = tf.constant([1,2,3])
matrix = tf.constant([[1,2],[3,4]])
```

---

# What is Keras?

Keras is TensorFlow's high-level API used for building, training, and evaluating neural networks with minimal code.

Advantages:
- Beginner Friendly
- Less Boilerplate Code
- Easy Model Building
- Supports CNNs, RNNs, Transformers, etc.

Import:

```python
from tensorflow import keras
```

---

# Sequential Model

Sequential is the simplest way to build a neural network.

It creates a **linear stack of layers**, where the output of one layer becomes the input of the next layer.

Architecture:

```
Input
   ↓
Flatten
   ↓
Dense
   ↓
Dropout
   ↓
Dense
   ↓
Output
```

Example:

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

model = Sequential([
    Flatten(input_shape=(28,28)),
    Dense(64, activation='relu'),
    Dense(10)
])
```

Use Sequential when:
- Single Input
- Single Output
- Layers connected one after another

---

# Dense Layer (Fully Connected Layer)

A Dense Layer is a layer where **every neuron is connected to every neuron in the previous layer.**

Each neuron computes:

```
z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
```

After computing z, an activation function is applied.

Example:

```python
Dense(64, activation='relu')
```

Meaning:
- 64 neurons
- ReLU activation
- Fully connected

---

# Input Layer

The Input layer defines the shape of the input data.

Example:

```python
Input(shape=(28,28))
```

For MNIST:
- Height = 28
- Width = 28

---

# Flatten Layer

Flatten converts multi-dimensional data into a one-dimensional vector.

Example:

```
28 × 28
↓

784
```

Code:

```python
Flatten()
```

Purpose:
Dense layers accept one-dimensional input.

---

# Activation Function

Activation functions introduce non-linearity into the neural network.

Common Activations

### ReLU

```
f(x)=max(0,x)
```

Used in hidden layers.

Example:

```python
Dense(64, activation='relu')
```

---

### Softmax

Converts outputs into probabilities.

Example:

```
[2.1,1.4,5.8]

↓

[0.03,0.01,0.96]
```

Usually used in the final classification layer.

---

# Dropout Layer

Dropout randomly turns off a percentage of neurons during training to reduce overfitting.

Example:

```python
Dropout(0.2)
```

Meaning:

20% neurons are randomly ignored during training.

---

# Model Compilation

Before training, TensorFlow must know:

- Optimizer
- Loss Function
- Evaluation Metric

Syntax:

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

compile() does **NOT** train the model.

It only configures how the model will learn.

---

# Optimizer

The optimizer updates the weights to minimize the loss.

Popular Optimizers:

- SGD
- Adam
- RMSProp

Example:

```python
from tensorflow.keras.optimizers import Adam

optimizer = Adam(learning_rate=0.001)
```

---

# Loss Function

Loss measures how wrong the model's predictions are.

Lower loss = Better predictions.

Examples:

Regression

```
Mean Squared Error (MSE)
```

Classification

```
Sparse Categorical Crossentropy
Categorical Crossentropy
Binary Crossentropy
```

---

# Metrics

Metrics evaluate model performance.

Examples:

```
Accuracy
Precision
Recall
F1 Score
```

Example:

```python
metrics=['accuracy']
```

---

# Training the Model

Training is done using:

```python
model.fit(X_train, y_train)
```

During training:

1. Forward Propagation
2. Loss Calculation
3. Backpropagation
4. Weight Update

---

# Epoch

An Epoch is **one complete pass of the entire training dataset through the neural network.**

Example:

```python
epochs=10
```

Meaning:

The model learns from the complete training dataset 10 times.

---

# Batch Size

Instead of training on all images at once, the dataset is divided into smaller batches.

Example:

```
60000 Images

↓

Batch Size = 32

↓

1875 batches
```

Advantages:
- Faster
- Less Memory
- Stable Learning

---

# Model Evaluation

Used after training.

Syntax:

```python
model.evaluate(X_test, y_test)
```

Returns:

```
Loss
Accuracy
```

Purpose:

Measures model performance on unseen data.

---

# Prediction

Used to make predictions on new data.

Syntax:

```python
prediction = model.predict(X_test)
```

Returns:

- Logits
or
- Probabilities

depending on the final layer.

---

# evaluate() vs predict()

| predict() | evaluate() |
|------------|------------|
| Makes predictions | Measures performance |
| Uses only X | Uses X and y |
| Returns predictions | Returns loss & accuracy |

---

# Normalization

Pixel values range from:

```
0 → 255
```

Normalize:

```python
X_train = X_train / 255.0
X_test = X_test / 255.0
```

Now values become:

```
0 → 0.0

255 → 1.0
```

Benefits:

- Faster Training
- Stable Gradient Descent
- Better Accuracy

---

# Typical TensorFlow Workflow

```
Import Libraries
      ↓
Load Dataset
      ↓
Normalize Data
      ↓
Create Model
      ↓
Compile Model
      ↓
Train Model
      ↓
Evaluate Model
      ↓
Predict New Data
```

---

# Complete Example

```python
import tensorflow as tf

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(
    optimizer='adam',
    loss=loss_fn,
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=10)

model.evaluate(X_test, y_test)

predictions = model.predict(X_test)
```

---