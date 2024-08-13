import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def pyschometricanalysis_function(csv_string):

  df  = pd.read_csv(r"C:\Users\Prannavakhanth\Documents\CareerPulse\psychometricanalysis_dataset.csv")

  columns = df.columns

  length = len(columns)


  results_set = columns[24: ]

  X = df[columns[: 24]]

  le = LabelEncoder()
  for i in columns[: 24]:
    X[i] = le.fit_transform(X[i])

  """#Optimism"""

  y = df[results_set[0]]

  Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

  model = DecisionTreeRegressor()
  model.fit(Xtrain, ytrain)
  predictions = model.predict(Xtest)

  print(accuracy_score(predictions, ytest))

  """#Self_Efficacy"""

  y = df[results_set[1]]

  Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

  model = DecisionTreeRegressor()
  model.fit(Xtrain, ytrain)
  predictions = model.predict(Xtest)

  print(accuracy_score(predictions, ytest))

  """#Resilience"""

  y = df[results_set[2]]

  Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

  model = DecisionTreeRegressor()
  model.fit(Xtrain, ytrain)
  predictions = model.predict(Xtest)

  print(accuracy_score(predictions, ytest))

  """#Stress_Tolerance"""

  y = df[results_set[3]]

  Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

  model = DecisionTreeRegressor()
  model.fit(Xtrain, ytrain)
  predictions = model.predict(Xtest)

  print(accuracy_score(predictions, ytest))

  """#Motivation"""

  y = df[results_set[4]]

  Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

  model = DecisionTreeRegressor()
  model.fit(Xtrain, ytrain)
  predictions = model.predict(Xtest)

  print(accuracy_score(predictions, ytest))

  """#Social_Skills"""

  y = df[results_set[4]]

  Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

  model = DecisionTreeRegressor()
  model.fit(Xtrain, ytrain)
  predictions = model.predict(Xtest)

  print(accuracy_score(predictions, ytest))

  """#Life_Satisfaction"""

  y = df[results_set[4]]

  Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

  model = DecisionTreeRegressor()
  model.fit(Xtrain, ytrain)
  predictions = model.predict(Xtest)


  column_dicts = {}

  for column in df.columns[: 24]:
      unique_values = df[column].unique()
      
      value_to_index = {value: index for index, value in enumerate(unique_values)}
      
      column_dicts[column] = value_to_index

output_list = []

user_input_df = pd.read_csv(r"C:\path\to\user_input.csv") 

answer_column = dataframe["Answer"]
question_column = dataframe["Question"]

answer_column_list = answer_column.tolist()
question_column_list = question_column.tolist()
 
for i in range(len(question_column_list)):
  if answer_column_list[i] in list(column_dicts[question_column_list[i]].keys) :
     output_list.append(column_dicts[question_column_list[i]][[column_dicts[question_column_list[i]].keys]])
     


  print(output_list)



pyschometricanalysis_function()
