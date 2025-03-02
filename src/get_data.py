from distutils.command.config import config
import shutil 
import os
import requests
import argparse
import yaml

def get_data(config_file):
  config=read_params(config_file)
  return config

# Calls read_params(config_file) to load the YAML config file.
# Returns the loaded configuration dictionary.

def read_params(config_file):
  with open(config_file) as yaml_file:
    config=yaml.safe_load(yaml_file)
  return config

# Opens the YAML file (params.yaml) and reads its content.
# Parses it using yaml.safe_load(), converting it into a Python dictionary.




def main():
  if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    get_data(config_file=parsed_args.config)

# --------------------------------------------Some notes----------------------------------

# This adds a command-line argument called --config, with a default value of 'params.yaml'.

# If the user provides a different file, it overrides the default.
# Example:
# bash
# Copy
# Edit
# python script.py --config custom.yaml
# ✅ Purpose: Allows the user to specify a custom config file.


# so if the user specifies python script.py --config custom.yaml here what does passed_args do ?
 
# ChatGPT said:
# If the user runs:

# bash
# Copy
# Edit
# python script.py --config custom.yaml
# 👉 passed_args will store the parsed arguments as an object.

# How passed_args Works in This Case?
# python
# Copy
# Edit
# passed_args = args.parse_args()
# ✅ This extracts the command-line argument and stores it as:

# python
# Copy
# Edit
# passed_args.config  # Contains 'custom.yaml'
# So when the script runs:

# python
# Copy
# Edit
# a = get_data(config_file=passed_args.config)
# 👉 It is equivalent to calling:

# python
# Copy
# Edit
# a = get_data(config_file="custom.yaml")
# 🔹 This means get_data() will load custom.yaml instead of params.yaml.