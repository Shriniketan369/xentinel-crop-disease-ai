from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

# Define Flask app
app = Flask(__name__)

# Absolute path to your Keras model
MODEL_PATH = r"E:\USA\Xentinel369\xentinel_model.keras"

# Load model
model = load_model(MODEL_PATH)

# Folder to save uploads
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def predict_crop_health(img_path):
    """Preprocess image and predict health."""
    img = image.load_img(img_path, target_size=(128, 128))  # match model input
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]

    # Binary classification logic — adjust if inverted
    if prediction < 0.5:
        result = "🌿 The plant appears **Healthy** ✅"
        confidence = 1 - prediction
    else:
        result = "⚠️ The plant appears **Diseased** 🚨"
        confidence = prediction

    return result, float(confidence)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            result, confidence = predict_crop_health(filepath)
            return render_template(
                'index.html',
                result=result,
                image_url=filepath,
                confidence=confidence
            )
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
