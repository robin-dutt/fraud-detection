import tensorflow as tf
from PIL import Image
import numpy as np

model = None
labels = ['real', 'fake']

def load_model():
    global model
    model = tf.keras.models.load_model('./fakevsreal_weights.h5')

def classify_image(file_path):
    if model is None:
        load_model()

    image = Image.open(file_path)
    image = image.resize((150, 150))
    image = image.convert("RGB")
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    
    # Predict the class (0 for real, 1 for fake)
    prediction = model.predict(image)
    return prediction[0][0]
