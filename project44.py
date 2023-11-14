import pandas as pd
import glob

# Set path to the folder containing CSV files
path = '/path/to/csv/files/*.csv'

# Use glob to get a list of all CSV files in the folder
files = glob.glob(path)

# Initialize an empty DataFrame to store the combined data
df = pd.DataFrame()

# Loop through the files and concatenate them into a single DataFrame
for file in files:
    temp_df = pd.read_csv(file)
    df = pd.concat([df, temp_df])

# Print the combined DataFrame
print(df)