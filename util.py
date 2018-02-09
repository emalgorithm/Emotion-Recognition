import scipy.io
import numpy as np
import math
import pandas as pd
from pandas import Series

def binarize_y(y, emotion_number):
	binary_y = y.copy()
	binary_y = binary_y.apply(lambda emotion: 1 if emotion == emotion_number else 0)

	return binary_y

def get_clean_dataframe():
	clean_data = scipy.io.loadmat('data/cleandata_students.mat')

	# clean_X and noisy_X are numpy matrixes with dimensions (# of training examples, number of features) containing training data
	clean_X = clean_data['x']

	# clean_Y and noisy_Y are numpy matrixes with dimensions (# of training examples, 1) 
	# clean_Y[k][0] contains the target emotion for training example k
	clean_y = np.array([array[0] for array in clean_data['y']])

	# clean_dataset is the pandas dataframe we will use to manipulate our data
	clean_dataset = pd.DataFrame(clean_X)
	clean_dataset[get_target()] = Series(clean_y, index=clean_dataset.index)

	return clean_dataset

def get_noisy_dataframe():
	noisy_data = scipy.io.loadmat('data/noisydata_students.mat')

	# clean_X and noisy_X are numpy matrixes with dimensions (# of training examples, number of features) containing training data
	noisy_X = noisy_data['x']

	# clean_Y and noisy_Y are numpy matrixes with dimensions (# of training examples, 1) 
	# clean_Y[k][0] contains the target emotion for training example k
	noisy_y = np.array([array[0] for array in noisy_data['y']])

	# noisy_dataset is the pandas dataframe we will use to manipulate our data
	noisy_dataset = pd.DataFrame(noisy_X)
	noisy_dataset[get_target()] = Series(noisy_y, index=noisy_dataset.index)	

	return noisy_dataset

def get_emotion_values():
	clean_data = scipy.io.loadmat('data/cleandata_students.mat')
	clean_y = np.array([array[0] for array in clean_data['y']])

	return list(set(clean_y))

def get_target():
	return 'emotion'

def get_predictors():
	clean_dataset = get_clean_dataframe()
	predictors = list(clean_dataset.columns)
	predictors.remove(get_target())

	return predictors