# %load q01_read_data/build.py
import yaml

def read_data():
    with open('../data/ipl_match.yaml') as f:
        data = yaml.load(f)
    # return data variable
    print data
    return data

read_data()
