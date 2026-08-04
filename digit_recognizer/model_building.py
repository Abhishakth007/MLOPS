from sklearn.linear_model import LogisticRegression


def model_builder(x_train , y_train):
	lr = LogisticRegression(max_iter = 1000)
	model = lr.fit(x_train , y_train.values.ravel())
	return model

	
