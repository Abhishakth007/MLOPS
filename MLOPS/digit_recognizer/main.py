from data_ingestion import data_loader

from data_staging import data_stager
from model_building import model_builder
from model_evaluation import model_evaluator

x_df,y_df = data_loader()

#print(x_df.head)
#print(y_df.head)

X_train , Y_train , X_test , Y_test = data_stager(x_df , y_df)
#print("X_Train:",len(X_train))
#print("Y_Train:",len(Y_train))
model= model_builder(X_train , Y_train)
print("Model Built")
#print(f"Model Built With Coefficients: {model.coef_}")
accuracy_score , report , cm = model_evaluator(model,X_test , Y_test)
print(accuracy_score , report , cm)





