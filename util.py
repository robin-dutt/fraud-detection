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
    image = image.resize((128, 128))
    image = image.convert("RGB")
    img = np.asarray(image)
    img = np.expand_dims(img, 0)
    predictions = model.predict(img)
    label = labels[np.argmax(predictions[0])]
    probab = float(round(predictions[0][np.argmax(predictions[0])] * 100, 2))

    result = {
        'label': label,
        'probability': probab  # Include probability in the result
    }

    return result
