import pandas as pd
import numpy as np
from dashboard.plot import getGraph, getAnotherGraph

import os
print(os.getcwd())

data = pd.read_csv('data.csv')
data["CLASS"] = data['y'] == 1
data["CLASS"] = data["CLASS"].astype('int')
data.pop('y')
data.pop('Unnamed: 0')

cols = data.columns.tolist()
cols = cols[-1:] + cols[:-1]

data = data[cols]

rows_pos = data['CLASS'] == 1
data_positive = data.loc[rows_pos]
data_negative = data.loc[~rows_pos]

positiveSamples = data_positive.sample(n=8)
negativeSamples = data_negative.sample(n=8)
randomSeizure = [np.array(row) for index, row in positiveSamples.iterrows()]
randomNonSeizure = [np.array(row) for index, row in negativeSamples.iterrows()]

freq = np.fft.fftfreq(178, 1./178)

randomSeizureFt = []
for row in randomSeizure:
    randomSeizureFt.append(np.abs(np.fft.fft(np.array(row[1:]))))
randomSeizureFt = pd.DataFrame(randomSeizureFt) 
randomSeizureFt = pd.concat([positiveSamples['CLASS'].reset_index(drop=True).astype('int32'), randomSeizureFt], axis=1)
randomSeizureFt = [np.array(row) for index, row in randomSeizureFt.iterrows()]

randomNonSeizureFt = []
for row in randomNonSeizure:
    randomNonSeizureFt.append(np.abs(np.fft.fft(np.array(row[1:]))))
randomNonSeizureFt = pd.DataFrame(randomNonSeizureFt)
randomNonSeizureFt = pd.concat([negativeSamples['CLASS'].reset_index(drop=True), randomNonSeizureFt], axis=1)
randomNonSeizureFt = [np.array(row) for index, row in randomNonSeizureFt.iterrows()]

def getSeizureHtml(col, data):
	x = []
	for i in range(1, 179):
		x.append(data[i])
	return getGraph(cols[1:], x, 1)

def getNonSeizureHtml(col, data):
	x = []
	for i in range(1, 179):
		x.append(data[i])
	return getGraph(cols[1:], x, 0)

def getColumns():
	return cols

def getSeizureData():
	return randomSeizure

def getNonSeizureData():
	return randomNonSeizure

def getFTColumns():
	return ['CLASS'] + list(freq)

def getSeizureFTData():
	return randomSeizureFt

def getNonSeizureFtData():
	return randomNonSeizureFt

def getSeizureFtHtml(data):
	x = []
	for i in range(1, 179):
		x.append(data[i])
	return getAnotherGraph(getFTColumns()[1:], x, 1)

def getNonSeizureFtHtml(data):
	x = []
	for i in range(1, 179):
		x.append(data[i])
	return getAnotherGraph(getFTColumns()[1:], x, 0)