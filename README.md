# 🔫 Gunshot Detection System (Custom Model)

This project is an **end-to-end Gunshot Detection System** built **from scratch** using Python.  
It detects gunshots from uploaded audio files, distinguishing them from background noise with **92% accuracy**.  
The system uses **Mel Spectrograms** for feature extraction, a custom-trained neural network model, and a **Flask-based backend** with a styled HTML/CSS/JS frontend.

---

## Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Dataset](#-dataset)
- [Model Training](#-model-training)
- [Directory Structure](#-directory-structure)
- [Tech Stack](#-tech-stack)
- [How to Run](#-how-to-run)
- [Future Improvements](#-future-improvements)
- [License](#-license)

---

## Overview
This system was designed to:
- **Identify gunshot sounds** from audio clips.
- Differentiate them from **other urban background noises**.
- Provide a simple **web interface** where users can upload audio files and instantly know if a gunshot is detected.

The model was **trained from scratch** (no pre-trained models used) on a dataset combining:
- **Urban8K Dataset**
- **YouTube GoPro Gunshot Compilations** (manually extracted clips)

---

## ✨ Features
- **Custom-trained deep learning model** with 92% accuracy.
- **Mel Spectrogram** feature extraction for better sound pattern recognition.
- **Flask backend** to handle file uploads and run model inference.
- **HTML/CSS/JavaScript frontend** with clean UI.
- Automatic storage of uploaded files for logging & analysis.

---

## Dataset
1. **UrbanSound8K Dataset** – Provided various urban environment sounds for non-gunshot examples.
2. **YouTube GoPro Gunshot Compilation** – Provided real-world gunshot examples.
3. Audio clips were cleaned, normalized, and converted to spectrograms for model input.

---

## Model Training
- Implemented in `crime_detector.ipynb`
- Steps:
  1. Preprocess audio → Generate Mel Spectrograms.
  2. Create labeled dataset (`Gunshot` / `Other`).
  3. Build and train a **custom CNN** model.
  4. Save trained model as `updated_gunshot_detection_model.h5`.

**Accuracy:** ~92% on test set.

---

## 📂 Directory Structure (Open the readme file to see the structure)
Gunshot-Detection/
│
├── user interface/
│ ├── templates/
│ │ ├── Model training/
│ │ │ ├── crime_detector.ipynb
│ │ │ ├── updated_gunshot_detection_model.h5
│ │ ├── gunshot_detected.html
│ │ ├── notrealfirst.html
│ ├── uploaded_files/ # Stores user-uploaded audio files
│ ├── backend2.py # Flask backend
│ ├── script.js # Frontend JS
│ ├── style.css # Frontend styles


---

## 🛠 Tech Stack
- **Python**
- **Flask** (Backend)
- **HTML / CSS / JavaScript** (Frontend)
- **NumPy, Librosa, Matplotlib** (Audio Processing)
- **TensorFlow / Keras** (Model Training)

---

## 🚀 How to Run
1. **Clone the repository**
```bash
git clone https://github.com/Batkhan/Gunshot-Detection-using-Model-created-from-scratch/new/master?filename=README.md
```
Run the Flask Server
```bash
python backend2.py
```
Open the address given by flask and run the application to get instant results

## ▶️ Youtube video Demo link

https://youtu.be/48MW6VxRHnk

📄 License
This project is licensed under the MIT License — you are free to use, modify, and distribute it with attribution.


