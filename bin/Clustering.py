# -*- encoding: utf-8 -*-
'''
@file: Clustering.py
@Author: Xuanlong
@email: qxlpku@gmail.com
''' 

# This file is used to cluster the cities based on the document embeddings

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler


def calculate_optimal_clusters(df, max_clusters=15):
    document_vectors = np.vstack(df['dimension'])
    bic_scores = []
    aic_scores = []

    for k in range(1, max_clusters + 1):
        gmm = GaussianMixture(n_components=k, random_state=42)
        gmm.fit(document_vectors)
        bic_scores.append(gmm.bic(document_vectors))
        aic_scores.append(gmm.aic(document_vectors))

    plt.figure(figsize=(8, 4))
    plt.plot(range(1, max_clusters + 1), bic_scores, 'bo-', label='BIC')
    plt.plot(range(1, max_clusters + 1), aic_scores, 'ro-', label='AIC')
    plt.xlabel('Number of Clusters, k')
    plt.ylabel('Information Criterion')
    plt.title('Information Theoretic Criteria for Cluster Determination')
    plt.legend()
    plt.grid(True)
    #save the plot
    plt.savefig('Five_Year_Plan/bin/doc/clusters/cluster_plot.png')
    # plt.show()

    optimal_k_BIC = np.argmin(bic_scores) + 1
    print("Optimal number of clusters (BIC):", optimal_k_BIC)

    optimal_k_AIC = np.argmin(aic_scores) + 1
    print("Optimal number of clusters (AIC):", optimal_k_AIC)

    return optimal_k_BIC, optimal_k_AIC


def cluster_cities(df, n_clusters):
    document_vectors = np.vstack(df['dimension'])
    scaler = StandardScaler()
    scaled_vectors = scaler.fit_transform(document_vectors)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(scaled_vectors)

    df['cluster_label'] = labels

    output_dir = 'Five_Year_Plan/bin/doc/clusters'
    os.makedirs(output_dir, exist_ok=True)
    
    for cluster_id in range(n_clusters):
        city_names = df[df['cluster_label'] == cluster_id]['cities'].tolist()
        # city_names = [name.split('_')[1:] for name in city_names]
        # city_names = ['_'.join(name) for name in city_names]
        
        print(f"Cluster {cluster_id}:")
        print(city_names)
        print(f"Cluster size: {len(city_names)}")
        print()
        
        with open(os.path.join(output_dir, f'cluster_{cluster_id}.txt'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(city_names))
    return df
    
if __name__ == '__main__':
    # the path of docments' vectors
    filePath = "Five_Year_Plan/bin/doc/Doc2vec_Models/tag_document_vecs_100v.pkl"
    
    # Load the data
    df = pd.read_pickle(filePath)
    print(df.head())

    bic,aic = calculate_optimal_clusters(df)
    cluster_cities(df, bic)

    
    
    
    
