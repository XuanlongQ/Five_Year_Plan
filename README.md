# Five_Year_Plan

## Main Work
This work use computational approaches to replicate Xu and Heikkila's paper and get some insights
- [How can cities learn from each other? Evidence from China's five-year plans](https://www.sciencedirect.com/science/article/pii/S2226585620300856)


## Datasets
1. The 12th Five Year Plan - 286 cities, you can get the dataset from [Here!](https://osf.io/ryph3/) under the folder under the folder /data/12th 5-yr plan_prefectures
2. The 27 Doc2vec models for Robustness check, you can get the dataset from [Here!](https://osf.io/ryph3/) under the folder /data/robustness check for doc2vec models

## Files
1. Doc2vec_model_training.py - Training Doc2vec model and get Doc2vec embeddings
2. Clustering.py - Using Doc2vec embeddings to conduct KMeans clustering
3. global_matching_algorithm.py - The algorithm for cluster matching
4. get_correlation_coefficient.py - Calculating the correlation coefficient for matched clusters

Note: Please remove the test.bin and all_docfiles.docx, which are placeholder Files.


## Acknowledge
- This replicated work was leaded by Prof. Eric j. Heikkila, Prof. Ling Zhu, and Prof. Ying XU.
- The team members include Xuanlong QIN and Runhui TIAN.
