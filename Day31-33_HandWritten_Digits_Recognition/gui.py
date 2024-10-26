import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *

# Load the dataset (Using MNIST dataset)
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize the data
train_images = train_images / 255.0
test_images = test_images / 255.0

# Reshaping to add channel dimension for CNN
train_images = np.expand_dims(train_images, axis=-1)
test_images = np.expand_dims(test_images, axis=-1)

# Model architecture
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')  # Output layer for 10 digits (0-9)
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(train_images, train_labels, epochs=5, validation_data=(test_images, test_labels))

# Save the model
model.save('handwritten_digit_model.h5')

# Function to recognize handwritten digits using the trained model
def predict_digit(image):
    # Preprocess the image for prediction
    img = np.expand_dims(image, axis=-1)  # Add a channel dimension for grayscale (28, 28, 1)
    img = img / 255.0  # Normalize the image like the training data
    img = img.reshape(1, 28, 28, 1)  # Reshape for model input
    res = model.predict([img])[0]
    return np.argmax(res), max(res)

# Display results for custom input (tkinter UI)
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Handwritten Digit Recognition")
        self.canvas = tk.Canvas(self, width=200, height=200, bg="white")
        self.canvas.pack()

        self.label = tk.Label(self, text="Draw a digit", font=("Helvetica", 20))
        self.label.pack()

        self.button_clear = tk.Button(self, text="Clear", command=self.clear_canvas)
        self.button_clear.pack()

        self.button_recognize = tk.Button(self, text="Recognize", command=self.recognize_digit)
        self.button_recognize.pack()

        self.canvas.bind("<B1-Motion>", self.draw)

        self.image = np.zeros((200, 200), dtype="uint8")

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x, y, x + 10, y + 10, fill="black")
        self.image[y:y + 10, x:x + 10] = 255

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = np.zeros((200, 200), dtype="uint8")

    def recognize_digit(self):
        img = self.image.copy()
        img = np.expand_dims(img, axis=-1)  # Add channel dimension for grayscale (200, 200, 1)
        img = tf.image.resize(img, (28, 28)).numpy().astype('uint8')  # Resize to 28x28
        digit, confidence = predict_digit(img)
        self.label.config(text=f'{digit}, {int(confidence * 100)}%')

# Run the tkinter app
if __name__ == "__main__":
    app = App()
    app.mainloop()
