from sklearn.datasets import load_digits
import pandas as pd
import numpy as np
import os
from pathlib import Path
def data_loader():
    digits = load_digits()
    #print(digits.keys())
    digits_data_df = pd.DataFrame(digits.data, columns = digits.feature_names)
    digits_target_df = pd.DataFrame(digits.target , columns = ['target'])
    #print(digits_data_df.head())
    #print(digits_target_df.head())
    print("Data Ingestion.Data_Loader returned 2 Dataframes")
    output_dir_path = Path.cwd()/"Exports"
    output_dir  = os.makedirs(output_dir_path, exist_ok=True)
    merged_df = pd.concat([digits_data_df , digits_target_df],axis = 1)
    raw_data_csv = merged_df.to_csv(output_dir_path/'raw.csv',index=False)
    return digits_data_df , digits_target_df

if __name__ == "__main__":
    raw_digits_data, raw_target_data = data_loader()

