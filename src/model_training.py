
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer

preprocessed_df = pd.read_csv('data/preprocessed_movies.csv')

features = ['budget', 'runtime', 'genre', 'rating', 'country']
target = 'gross'

imputer = SimpleImputer(strategy='mean')
preprocessed_df[features] = imputer.fit_transform(preprocessed_df[features])

X_train, X_test, y_train, y_test = train_test_split(preprocessed_df[features], preprocessed_df[target], test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

train_preds = model.predict(X_train)
train_rmse = mean_squared_error(y_train, train_preds, squared=False)
print(f"Train RMSE: {train_rmse}")
test_preds = model.predict(X_test)
test_rmse = mean_squared_error(y_test, test_preds, squared=False)
print(f"Test RMSE: {test_rmse}")

import joblib
joblib.dump(model, 'trained_model.pkl')

