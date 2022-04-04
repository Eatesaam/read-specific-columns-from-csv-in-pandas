import pandas as pd


# provide column names that is required to get data from csv
col_list = ["firstname", "lastname","message"]
# read csv data from csv file with spesific columns
csv_data = pd.read_csv("test.csv", usecols=col_list )
print(csv_data)
# convert csv data of pandas dataframe to json
csv_data.to_json("test.json", orient='records')

