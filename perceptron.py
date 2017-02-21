import numpy as np

def add_bias_param(X):
	X = np.array(X)
	bX = np.zeros( (X.shape[0], X.shape[1] + 1) )
	for r in range(len(X)):
		bX[r][0] = 1
		for c in range(len(X[r])):
			bX[r][c + 1] = X[r][c]
	return bX


def linear_activation(wts, x):
	return np.dot(wts, x)


def logistic_activation(wts, x):
	dp = linear_activation(wts, x)
	return np.power(np.e, dp) / (1.0 + np.power(np.e, dp))


class Perceptron(object):
	def __init__(self, activation=logistic_activation):
		self.wts = None
		self.activation = activation


	def intercept(self):
		return self.wts[0]


	def coefs(self):
		return self.wts[1:]


	def update_wts(self, X, Y):
		for r in range(X.shape[0]):
			y = self.activation(self.wts, X[r])
			d = Y[r]
			new_wts = np.array(self.wts)
			for f in range(X.shape[1]):
				new_wts[f] = self.wts[f] + (d - y) * X[r][f]
			self.wts = new_wts


	def fit(self, X, Y, _iter=5):
		X = add_bias_param(X)
		self.wts = np.zeros(len(X[0]))
		for _ in range(_iter):
			self.update_wts(X, Y)


	def activation_vals(self, X):
		X = add_bias_param(X)
		A = np.dot(X, self.wts)
		return np.array([np.sum(a) for a in A])


	def predict(self, X):
		A = self.activation_vals(X)
		P = np.zeros(len(X), dtype=int)
		for i in range(len(P)):
			if A[i] > 0:
				P[i] = 1
			else:
				P[i] = 0
		return P
