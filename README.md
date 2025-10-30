# 🌱 Xentinel — AI Crop Health Detection System

**Xentinel** is an AI-powered web application that detects whether a crop leaf is *Healthy* or *Diseased*, it aims to help small-scale farmers prevent crop losses using accessible AI tools.

---

## 🧠 Overview
Xentinel uses a **Convolutional Neural Network (CNN)** trained on open-source datasets of **Tomato** (**Chilli and cotton** in progress) crops.  
The system performs **binary classification (Healthy vs Diseased)** and provides a confidence score for each prediction.

---

## ⚙️ Tech Stack
- **TensorFlow / Keras** — CNN model training  
- **Flask** — Web framework for deployment  
- **OpenCV** — Image preprocessing  
- **HTML, CSS, JavaScript** — Frontend interface  

---

## 🧩 Model Details
- Input shape: **(128, 128, 3)**
- Activation: ReLU + Sigmoid (final)
- Output: 1 neuron for binary classification
- Accuracy: **~94%** on validation dataset

---

