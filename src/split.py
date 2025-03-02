import shutil 
import yaml
import pandas as pd
import numpy as np
import os 
from get_data import get_data,read_params
import argparse
from sklearn.model_selection import train_test_split
def split(config_file):
    config=get_data(config_file)
    root_dir=config['load_data']['raw_data']
    train_path=config['model']['train_path']
    test_path=config['model']['test_path']

    categories=[d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir,d))]
    for category in categories:
        img_path=os.path.join(root_dir,category)
        images=os.listdir(img_path)#ithun dar category sathi sagle images load hotil 

        train_images,test_images=train_test_split(images,test_size=0.2,random_state=42)
        os.makedirs(os.path.join(train_path, category), exist_ok=True)
        os.makedirs(os.path.join(test_path, category), exist_ok=True)

        for img in train_images:
            shutil.copy(os.path.join(img_path,img),os.path.join(train_path,category,img))
            
        for img in test_images:    
            shutil.copy(os.path.join(img_path,img),os.path.join(test_path,category,img))

    
    print("Split the images successfully :D")






if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    split(config_file=parsed_args.config)