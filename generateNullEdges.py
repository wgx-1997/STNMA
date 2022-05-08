import networkx as nx
import numpy as np
import random as rd
from sklearn.model_selection import train_test_split

DATA_DIR = 'input/'
# DATASET_NAME = 'WikiElec'
REMAIN = 60
SEED = 16
# test_size = 0.2


# datasets = ['WikiElec', 'WikiRfa', 'Slashdot', 'Alpha', 'OTC']
# test_sizes = [0.2, 0.4, 0.6]
datasets = ['WikiElec']
test_sizes = [0.3, 0.5, 0.7]
for DATASET_NAME in datasets:
    for test_size in test_sizes:
        G = nx.DiGraph()
        with open(DATA_DIR + DATASET_NAME + '.txt') as f:
            for line in f:
                line = line.strip().split('\t')
                line = list(map(int, line))
                G.add_edge(line[0], line[1], weight=line[2])
        numNodes = max(G.nodes) + 1
        G.add_nodes_from(range(numNodes))

        lenTrainSet = 0
        with open(DATA_DIR + DATASET_NAME + '/%s-%g-train.txt' % (DATASET_NAME, test_size)) as f:
            for line in f:
                lenTrainSet += 1

        lenTestSet = 0
        with open(DATA_DIR + DATASET_NAME + '/%s-%g-test.txt' % (DATASET_NAME, test_size)) as f:
            for line in f:
                lenTestSet += 1

        train_edges_null, test_edges_null = [], []
        for _ in range(3 * lenTestSet):
            u = rd.choice(range(numNodes))
            v = rd.choice(range(numNodes))
            while v in list(G.successors(u)):
                v = rd.choice(range(numNodes))
            test_edges_null.append([u, v, 99])
        for _ in range(3 * lenTrainSet):
            u = rd.choice(range(numNodes))
            v = rd.choice(range(numNodes))
            while v in list(G.successors(u)):
                v = rd.choice(range(numNodes))
            train_edges_null.append([u, v, 99])

        with open(DATA_DIR + DATASET_NAME + '/null-%s-%g-train.txt' % (DATASET_NAME, test_size), 'w') as f:
            for edge in train_edges_null:
                f.write(str(edge[0]) + '\t' + str(edge[1]) + '\t' + str(edge[2]) + '\n')

        with open(DATA_DIR + DATASET_NAME + '/null-%s-%g-test.txt' % (DATASET_NAME, test_size), 'w') as f:
            for edge in test_edges_null:
                f.write(str(edge[0]) + '\t' + str(edge[1]) + '\t' + str(edge[2]) + '\n')