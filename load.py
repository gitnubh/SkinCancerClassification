# import the necesary libraries
import tensorflow as tf
import os
from keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# define labels
def get_label_name(class_index):
    if class_index == 0:
        return "Carcinogenic"
    else:
        return "Non-Carcinogenic"

# path to the ml model
skicc_model = tf.keras.models.load_model('path/to/model')
