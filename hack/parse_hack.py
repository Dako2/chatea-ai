import glob
import pandas as pd
import json
import tiktoken
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
    
encoding = tiktoken.get_encoding("cl100k_base")
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
encoding.encode("tiktoken is great!")

# Get a list of CSV file paths
fns = glob.glob("*.csv")

# Create an empty DataFrame to concatenate data
df0 = pd.DataFrame()

# Concatenate data from all CSV files into df0
for fn in fns:
    df = pd.read_csv(fn)
    df0 = pd.concat([df0, df])

# Define the instruction for JSON data
instruction = "患者姓名\t病症\t治疗方案，复诊，和治疗效果"

# Create a list to store JSON data
data_output = []

# Iterate over rows in df0
for index, row in df0.iterrows():
    try:
        # Prepare the data dictionary
        temp = row['Details'].replace('sstp上海科学技术出版社nihao', '').split('\n')[1].replace('\t',' ')
        #data = {'text':f'[INST] {instruction}\t{temp} [/INST]'}
        data = {"keywords": row['Title'], "details": row['Details'].replace('sstp上海科学技术出版社nihao', '').split('\n')[1]}

        # Add the data dictionary to the output list
        data_output.append(data)
    except:
        continue

# Optionally, you can also save the entire list of data_output to a JSON file with indentation
with open("hackathon_xingyuanlin_all_data.json", "w", encoding="utf-8") as json_file:
    json.dump(data_output, json_file, ensure_ascii=False, indent=4)
