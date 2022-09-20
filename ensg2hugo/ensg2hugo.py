#!/usr/bin/python
import re
import pandas as pd
import argparse

dict_e2h={}
with open('gencode.v41.basic.annotation.gtf', 'r') as file:
    for line in file:
         re_e2h=re.search('.*gene_id "(.*?)".*gene_name "(.*?)";',line)
         if re_e2h:
            dict_e2h[re_e2h.group(1).split('.')[0]]=re_e2h.group(2)

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-f',type=int,default=1,choices=range(10))
parser.add_argument('file',type=str)
df = pd.read_csv(parser.parse_args().file, sep='\t')
col_num = parser.parse_args().f - 1
df.iloc[:,col_num] = df.iloc[:,col_num].map(lambda x: x.split('.')[0])

def en2ho(gene_id):
    if gene_id in dict_e2h.keys():
        return dict_e2h[gene_id]
    else:
        return gene_id

df.iloc[:,col_num]= df.iloc[:,col_num].map(lambda x: en2ho(x))
df.to_csv('./expression_analysis.hugo.tsv',sep='\t')
