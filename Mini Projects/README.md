# 🧠 MNIST Handwritten Digit Recognition

This mini-project implements a Convolutional Neural Network (CNN) using TensorFlow and Keras to recognize handwritten digits from the MNIST dataset. The model is trained with data augmentation for better generalization and includes functionality to predict digits from uploaded images.

---

## 📌 Features

- Trains on MNIST dataset (handwritten digits 0–9)
- Uses data augmentation (rotation, shift, zoom) to improve accuracy
- Efficient CNN architecture with dropout & batch normalization
- Predict digits from user-uploaded images
- Saves the trained model in the `.keras` format

---

## 🗂️ Dataset

- Dataset: [MNIST Handwritten Digits](http://yann.lecun.com/exdb/mnist/)
- Training samples used: 20,000 (reduced for faster training)
- Testing samples used: 5,000

---

## 🧠 Model Architecture

```text
Input: 28x28 grayscale image

Conv2D(32) → BatchNorm → MaxPooling → Dropout(0.25)
Conv2D(64) → BatchNorm → MaxPooling → Dropout(0.25)
Conv2D(128) → BatchNorm → MaxPooling → Dropout(0.4)
Flatten
Dense(256, ReLU) → BatchNorm → Dropout(0.5)
Dense(10, Softmax)
```

🧪 Training Details
Optimizer: Adam (learning_rate=0.0005)

Loss Function: Sparse Categorical Crossentropy

Batch Size: 64

Epochs: 5

Data Augmentation:

rotation_range=10

width_shift_range=0.1

height_shift_range=0.1

zoom_range=0.1

📊 Results
Validation Accuracy after training: ~98% (depending on session)

Model is saved as mnist_digit_model.keras

🚀 Usage
🔧 Prerequisites
Make sure the following libraries are installed:

pip install tensorflow numpy matplotlib opencv-python pillow
🏁 Running the Project
Train the model (if not already saved):

model.fit(...)
model.save("mnist_digit_model.keras")
Upload and predict digit from your image:

upload_and_predict()
Upload a grayscale image (28x28 recommended)

The model predicts and prints the digit

📸 Example Prediction
After uploading a digit image:

🔢 Predicted digit: 3

🧰 File Structure
├── train_model.py             # Contains training and model saving logic
├── upload_predict.py          # Handles image upload and digit prediction
├── mnist_digit_model.keras    # Saved trained model
