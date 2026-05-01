import numpy as np

eig_ones = np.linalg.eig([[1,1],[1,1]])
eig_ones = np.linalg.eig(
    [[1,1,1],
     [1,1,1],
     [1,1,1]])

print(f"eig_ones - eigen*values* = \n{np.round(eig_ones.eigenvalues.real, 10)}\n")
print(f"eig_ones - eigen*vectors* = \n{eig_ones.eigenvectors}\n")

#######################

from sklearn.decomposition import PCA
X = np.array(
    [[-1, -1], 
     [-2, -1], 
     [-3, -2], 
     [1, 1], 
     [2, 1], 
     [3, 2]])

pca = PCA(n_components=2)
pca.fit(X)

print(pca.explained_variance_ratio_)

print(pca.singular_values_)

pca = PCA(n_components=2, svd_solver='full')
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.singular_values_)

pca = PCA(n_components=1, svd_solver='arpack')
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.singular_values_)