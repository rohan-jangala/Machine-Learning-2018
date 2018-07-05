import numpy as np
import tflearn

from tflearn.data_utils import load_csv
data, labels = load_csv('crypto-markets.csv', target_column = 8, columns_to_ignore = [0, 2, 3], categorical_labels = True, n_classes = 2)

net = tflearn.input_data(shape=[None,6])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 2, activation='sigmoid')
net = tflearn.regression(net)

model = tflearn.DNN(net)
model.fit(data, labels, n_epoch=100, batch_size=30, show_metric=True)