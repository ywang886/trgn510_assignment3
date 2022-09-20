#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-f',type=int,default=1,choices=range(10))
parser.add_argument('file',type=str)
filename=parser.parse_args().file
col_num=parser.parse_args().f
df = pd.read_csv(filename, sep='\t', usecols=[col_num])
col_name = df.columns[0]
plt.hist(df)
plt.title(col_name)
plt.xlabel(col_name)
plt.ylabel('number')
plt.savefig('./' + col_name + '_heart.png')
