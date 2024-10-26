import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load the dataset (Using MNIST or a custom dataset)
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize the data
train_images = train_images / 255.0
test_images = test_images / 255.0

# Reshaping to add channel dimension for CNN
train_images = np.expand_dims(train_images, axis=-1)
test_images = np.expand_dims(test_images, axis=-1)

# Data augmentation
data_gen = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1
)
data_gen.fit(train_images)

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
history = model.fit(data_gen.flow(train_images, train_labels, batch_size=32), 
                    epochs=15, 
                    validation_data=(test_images, test_labels))

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc}')

# Save the model
model.save('handwritten_digit_model.h5')

# Function to recognize handwritten digits using the trained model
def predict_digit(image):
    img = image.reshape(1, 28, 28, 1)  # Reshape for model input
    img = img / 255.0  # Normalize the image
    res = model.predict([img])[0]
    return np.argmax(res), max(res)

# Display results for custom input (implement UI using tkinter)
import tkinter as tk
from tkinter import *

# Create tkinter GUI for drawing digits
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
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
        self.canvas.create_oval(x, y, x+10, y+10, fill="black")
        self.image[y:y+10, x:x+10] = 255

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = np.zeros((200, 200), dtype="uint8")

    def recognize_digit(self):
        img = self.image.copy()
        img = np.expand_dims(img, axis=-1)  # Add channel dimension for grayscale
        img = tf.image.resize(img, (28, 28)).numpy().astype('uint8')  # Resize image to 28x28
        digit, confidence = predict_digit(img)
        self.label.config(text=f'{digit}, {int(confidence * 100)}%')


# Run the tkinter app
if __name__ == "__main__":
    app = App()
    app.mainloop()
