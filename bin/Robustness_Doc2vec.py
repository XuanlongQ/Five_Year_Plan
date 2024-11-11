# -*- encoding: utf-8 -*-
'''
@file: Robustness check for Doc2vec model.py
@Author: Xuanlong
@email: qxlpku@gmail.com
''' 
# Chi-square test for robustness of Doc2vec model
import pandas as pd
from scipy.stats import chi2_contingency


def check_city_names_match(file_path1, file_path2):
    # get data
    df1 = pd.read_csv(file_path1)
    df2 = pd.read_csv(file_path2)
    
    # make sure all 'city_name' is lower case
    df1['city_name'] = df1['city_name'].str.lower()
    df2['city_name'] = df2['city_name'].str.lower()
    
    # get the lists
    cities1 = set(df1['city_name'])
    cities2 = set(df2['city_name'])
    
    for _ in cities1:
        print(_)
    
    # check whether these two lists are consistence
    if cities1 == cities2:
        print("All city names match between the two files.")
    else:
        print("City names do not match.")
        print("Cities in file1 not in file2:", cities1 - cities2)
        print("Cities in file2 not in file1:", cities2 - cities1)

def perform_chi_square_test(file1_path, file2_path):
    """
    kai-square
    
    para:
    file1_path (str): 
    file2_path (str): 
    
    return: dict
    """
  
    data1 = pd.read_csv(file1_path)
    data2 = pd.read_csv(file2_path)
    
    data1['city_name'] = data1['city_name'].str.replace('_', '').str.lower()
    data2['city_name'] = data2['city_name'].str.replace('_', '').str.lower()

    data_merged = pd.merge(data1, data2, on='city_name', suffixes=('_file1', '_file2'))
    print(data1.shape, data2.shape, data_merged.shape,print(data_merged.head()))
    
  
    contingency_table = pd.crosstab(data_merged['cluster_id_file1'], data_merged['cluster_id_file2'])

    chi2, p, dof, expected = chi2_contingency(contingency_table)

    return {
        "Chi-square value": chi2,
        "P-value": p,
        "Degrees of freedom": dof,
        "Expected frequencies": expected
    }
    

if __name__ == "__main__":
    file_path1 = 'Five_Year_Plan/bin/doc/clusters/Xu-Heikkila.txt'
    file_path2 = 'Five_Year_Plan/bin/doc/clusters/100v5w7mc.txt'
    # check_city_names_match(file_path1, file_path2)
    
    results = perform_chi_square_test(file_path1, file_path2)

    print("Chi-square value:", results["Chi-square value"])
    print("P-value:", results["P-value"])
    print("Degrees of freedom:", results["Degrees of freedom"])
    print("Expected frequencies:\n", results["Expected frequencies"])