# Read the data from data source
# Save it in the data\raw fro the furthur process
'''

from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    #print(df)
    new_cols = [col.replace(" ","_") for col in df.columns]
    
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    
    df.to_csv(raw_data_path,sep = ",", index= False, header = new_cols)
    
if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default = "params.yaml")
    #parsed_args = args.parse_args()
    parsed_args, unknown = args.parse_known_args()
    load_and_save(config_path = parsed_args.config)
    
 '''

import os
os.chdir(r"C:\Users\harde\OneDrive\Documents\New & Updated Documents\Documents\Documents\MLOpsProject\data_given")

import pandas as pd
df = pd.read_csv("winequality.csv")
#df.columns
new_cols = [col.replace(" ","_") for col in df.columns]

df.columns = new_cols

# Changing the directory
os.chdir(r"C:\Users\harde\OneDrive\Documents\New & Updated Documents\Documents\Documents\MLOpsProject\data\raw")

df.to_csv("winequality.csv",encoding = 'utf-8',sep = ",", index= False)



