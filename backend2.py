from flask import Flask, request, jsonify, send_from_directory, render_template
import os
import numpy as np
from keras.models import load_model
import librosa
import resampy

app = Flask(__name__)

# Load the pre-trained model
model_path = "C:/Users/batma/OneDrive/Documents/crime detector main/updated_gunshot_detection_model.h5"
new_model1 = load_model(model_path)

# Define the directory for uploaded files
upload_dir = "C:/Users/batma/OneDrive/Pictures/User inteface/uploaded_files"
template_dir = "C:/Users/batma/OneDrive/Pictures/User inteface/templates"

# Function to predict if it's a gunshot or not
def prediction_parser(audio_file_path, model):
    global f
    f=0
    audiodata, sample_rate = librosa.load(audio_file_path, res_type='kaiser_fast') 
    mels = np.mean(librosa.feature.melspectrogram(y=audiodata, sr=sample_rate).T, axis=0)
    X = mels.reshape(1, -1)
    class_id = np.argmax(model.predict(X))
    prediction = 'Gunshot' if class_id == 1 else 'Non-Gunshot'
    if class_id==1:
        f=1
    return prediction
@app.route("/")
def get_html():
    return send_from_directory(template_dir, "nottherealfirst.html")
print('hello')
# Route to handle file upload
@app.route("/upload/", methods=["POST"])
def upload_file():
    file = request.files["file"]
    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)
    return jsonify({"message": "File uploaded successfully.", "filename": file_path})

# Route to predict if it's a gunshot or not
@app.route("/predict/", methods=["POST"])
def predict():
    file = request.files["file"]
    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)
    prediction = prediction_parser(file_path, new_model1)
    print(prediction)
    if f==1:
        gunshot_detected()
        return jsonify({"prediction": prediction})
    else:
        return jsonify({"prediction": prediction})

# Route to display "Gunshot Detected" message
@app.route("/gunshot_detected")
def gunshot_detected():
    return send_from_directory(template_dir, "gunshot_detected.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
