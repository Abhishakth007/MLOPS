
from sklearn.metrics import accuracy_score , classification_report , confusion_matrix

def model_evaluator(model , x_test , y_test):
	
	results = model.predict(x_test)
	acc_score = accuracy_score(y_test , results)
	report = classification_report(y_test , results)
	cm = confusion_matrix(y_test , results)
	print("Model Evaluated")
	return acc_score , report , cm



