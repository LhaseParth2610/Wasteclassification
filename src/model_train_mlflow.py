import os
import requests
import argparse
from keras.layers import Dense,Flatten,Conv2D,Maxpooling 
from keras.model import load_model,Model
from sklearn.metrics import classification_report,confusion_matrix
from get_data import get_data
from keras_preprocessing.image import ImageDataGenerator
import pandas as pd
import numpy as np
import seaborn as sns

def model_train_mlflow(config_file):
    config=get_data(config_file)
    train_path=config['model'][]





if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config',default='params.yaml')
    passed_args = args_parser.parse_args()
    model_train_mlflow(config_file=passed_args.config)