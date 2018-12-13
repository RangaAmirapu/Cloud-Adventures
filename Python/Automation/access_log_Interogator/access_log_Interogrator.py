import pandas as pd
import argparse
import json

parser=argparse.ArgumentParser()
parser.add_argument("-f", help = "json formatted log file path")

args=parser.parse_args()

# read json file line by line and remove /n delimiter at end of each line 
# with open('access_log.json', 'r') as f:
#     distros_dict = json.load(f)

# for distro in distros_dict:
#     print(distro['remote_host'])


data_df = pd.read_json(args.f, lines=True)

print(data_df)





