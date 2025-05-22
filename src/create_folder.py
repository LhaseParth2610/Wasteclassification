
import os 


import requests
from get_data import get_data,read_params
import yaml 
import shutil
import pandas as pd
import numpy  as np
import argparse
def create_folders(config_file):
    config=get_data(config_file)
    preprocessed_data_path=config['load_data']['preprocessed_data']
    raw_data_path=config['load_data']['raw_data']
    classes=config['load_data']['num_classes']

    categories=[d for d in os.listdir(raw_data_path)if os.path.isdir(os.path.join(raw_data_path,d))]
    #if condition to make usre we include dir's and not files also the the join part,os.path.join("data/raw", "plastic")  → "data/raw/plastic"
    

    os.makedirs(os.path.join(preprocessed_data_path,'train'),exist_ok=True)
    os.makedirs(os.path.join(preprocessed_data_path,'test'),exist_ok=True)

    for category in categories:
        os.mkdir(os.path.join(preprocessed_data_path,"train",category))
        os.mkdir(os.path.join(preprocessed_data_path,"test",category))

    print("Done Creating Folder :D " )


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument('--config',default="params.yaml")
    parsed_args=args.parse_args()
    create_folders(config_file=parsed_args.config)
       