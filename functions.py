import numpy as np
import math

from enum import Enum

@unique
static class Column(Enum):
  DATE = 0
  OPEN = 1
  HIGH = 2
  LOW = 3
  CLOSE = 4
  ADJCLOSE = 5
  VOLUME = 6

# prints formatted price
def formatPrice(n):
	return ("-$" if n < 0 else "$") + "{0:.2f}".format(abs(n))

# returns the vector containing stock data from a fixed file
def getStockDataVec(key, Column=4):
	vec = []
	lines = open("data/" + key + ".csv", "r").read().splitlines()
	for line in lines[1:]:
    tval = line.split(",")
    #Date,Open,High,Low,Close,Adj Close,Volume
		vec.append(float(tval[Column]))

	return vec

# returns the sigmoid
def sigmoid(x):
	try:
		if x < 0:
			return 1 - 1 / (1 + math.exp(x))
		return 1 / (1 + math.exp(-x))
	except OverflowError as err:
		print("Overflow err: {0} - Val of x: {1}".format(err, x))
	except ZeroDivisionError:
		print("division by zero!")
	except Exception as err:
		print("Error in sigmoid: " + err)
	

# returns an an n-day state representation ending at time t
def getState(data, t, n):
	d = t - n + 1
	block = data[d:t + 1] if d >= 0 else -d * [data[0]] + data[0:t + 1] # pad with t0
	res = []
	for i in range(n - 1):
		res.append(sigmoid(block[i + 1] - block[i]))

	return np.array([res])
