import tensorflow as tf

def load_model_ml():
    return tf.keras.models.load_model('degreesml/ml_model/celsius_a_fahrenheit.h5')

model_ml = load_model_ml()