import numpy as np
import tflearn

from tflearn.datasets import titanic
titanic.download_dataset('titanic-dataset.csv')

from tflearn.data_utils import load_csv
data, labels = load_csv('titanic-dataset.csv', target_column = 0, columns_to_ignore = [2, 7], categorical_labels = True, n_classes = 2)