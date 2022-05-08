import networkx as nx
import numpy as np
from sklearn.model_selection import train_test_split
import sys

seed = 16

def read_edge_list(edge_path):
    G = nx.DiGraph()
    edges = np.loadtxt(edge_path)
    for i in range(edges.shape[0]):
        G.add_edge(int(edges[i][0]), int(edges[i][1]), weight=edges[i][2])
    edges = [[e[0], e[1], e[2]['weight']] for e in G.edges.data()]
    return edges, max(G.nodes) + 1  # index can start from 0.

def split_dataset(edge_path, test_size):
    edges, _ = read_edge_list(edge_path)
    train_edges, test_edges = train_test_split(edges, test_size=test_size, random_state = seed)
    datadir = edge_path.split('.')[0] + '-%g-' % (test_size)
    np.savetxt(datadir + 'train.txt', train_edges, fmt='%i', delimiter='\t')
    np.savetxt(datadir + 'test.txt', test_edges, fmt='%i', delimiter='\t')

if __name__ == '__main__':
    # datasets = ['WikiElec', 'WikiRfa', 'Slashdot', 'Alpha', 'OTC']
    # test_sizes = [0.2, 0.4, 0.6]
    datasets = ['WikiElec']
    test_sizes = [0.3, 0.5, 0.7]
    for dataset in datasets:
        for test_size in test_sizes:
            split_dataset('input/%s/%s.txt' % (dataset, dataset), test_size)