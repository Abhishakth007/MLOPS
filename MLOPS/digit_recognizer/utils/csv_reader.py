import pandas as pd

path_to_file = "/home/ubuntu/MLOPS/digit_recognizer/Exports/raw.csv"

data = pd.read_csv(path_to_file)
df = pd.DataFrame(data)
print(df.head)
