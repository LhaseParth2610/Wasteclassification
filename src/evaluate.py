from distutils.command.config import config
import shutil 
import os
import requests
import argparse
import yaml
from keras.model import load_model
from sklearn.metrics import classification_report,confusion_matrix
from get_data import get_data
from keras_preprocessing.image import ImageDataGenerator
import pandas as pd
import numpy as np
import seaborn as sns

def evaluate(config_file):
    config=get_data(config_file)
    batch=config['img_augment']['batch_size']
    test_path=config['model']['test_path']
    class_mode=['img_augment']['class_mode']
    model=load_model('saved_models/trained.h5')
    config=get_data(config_file)

    test_gen=ImageDataGenerator(rescale=1./255)
    test_set=test_gen.flow_direectory(test_path,
                                      target_size=(225,225),
                                      batch_size=batch,
                                      class_mode=class_mode
                                      )
    label_map=(test_set.class_indices)
    print(label_map)
    Y_pred = model.predict(test_set, len(test_set))
    y_pred = np.argmax(Y_pred, axis=1)

# Y_pred = model.predict(test_set, len(test_set))	Generates class probabilities for all test images
# y_pred = np.argmax(Y_pred, axis=1)	Converts probabilities to final predicted class labels
#Y_pred = [[0.1, 0.7, 0.05, 0.05, 0.1],  # Image 1 (Highest = Class 1)
        #   [0.6, 0.1, 0.1, 0.1, 0.1],  # Image 2 (Highest = Class 0)
        #   [0.05, 0.05, 0.05, 0.8, 0.05]]  # Image 3 (Highest = Class 3)
    print("Confusion Matrix")
    sns.heatmap(confusion_matrix(test_set.classes,y_pred),annot=True)

    print("Classification Report")
    target_names = ['cardboard','glass','metal','paper','plastic','trash']
    df =pd.DataFrame(classification_report(test_set.classes, y_pred, target_names=target_names, output_dict=True)).T
    df['support']=df.support.apply(int)
    df.style.background_gradient(cmap='viridis',subset=pd.IndexSlice['0':'9','f1-score'])
    df.to_csv('reports/classification_report')
    print('Classification Report and Confusion Matrix Report are saved in reports folder of Template')






if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config',default='params.yaml')
    passed_args = args_parser.parse_args()
    evaluate(config_file=passed_args.config)