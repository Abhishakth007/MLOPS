from sklearn.model_selection import train_test_split
import pandas as pd
import os
from pathlib import Path

def data_stager(data_df , target_df):
    x_train ,x_test , y_train, y_test = train_test_split(data_df , target_df , test_size = 0.3,random_state = 1)
    print("Data Staged")
    output_dir_path = path.cwd()/"Exports"
    x_train_df = pd.DataFrame(x_train).to_csv(output_dir_path/"xtrain.csv")
    y_train_df = pd.DataFrame(y_train).to_csv(output_dir_path/"ytrain.csv")
    x_test_df = pd.DataFrame(x_test).to_csv(output_dir_path/"xtest.csv")
    y_test_df = pd.DataFrame(y_test).to_csv(output_dir_path/"ytest.csv")

    return x_train , y_train , x_test , y_test
