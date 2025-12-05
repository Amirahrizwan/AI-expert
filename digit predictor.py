import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load MNIST dataset
# -----------------------------
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize data (0-255 → 0-1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# -----------------------------
# 2. Build model
# -----------------------------
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# -----------------------------
# 3. Train model
# -----------------------------
print("Training model…")
model.fit(x_train, y_train, epochs=5)

# Evaluate
loss, acc = model.evaluate(x_test, y_test)
print(f"\nModel Accuracy: {acc*100:.2f}%")

# -----------------------------
# 4. Function to predict digit from image
# -----------------------------
def predict_digit(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("❌ Image not found.")
        return

    # Resize to 28x28 (MNIST size)
    img = cv2.resize(img, (28, 28))

    # Invert colors if background is white
    if img.mean() > 127:
        img = 255 - img

    # Normalize and reshape
    img = img / 255.0
    img = img.reshape(1, 28, 28)

    # Predict
    prediction = model.predict(img)
    digit = np.argmax(prediction)

    # Show result
    plt.imshow(img.reshape(28, 28), cmap='gray')
    plt.title(f"Predicted Digit: {digit}")
    plt.axis('off')
    plt.show()

    print(f"Predicted Digit: {digit}")

# -----------------------------
# 5. CALL THE FUNCTION
# -----------------------------

# Example: Place your digit image as 'digit.png'
predict_digit("digit.png")
