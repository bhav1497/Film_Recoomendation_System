import unittest
from model_training import model, mean_squared_error
from sklearn.metrics import mean_squared_error as sk_mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd

class TestModelTraining(unittest.TestCase):
    def test_model_training(self):
        
        data = {
            'budget': [100, 200, 300, 400, 500],
            'runtime': [120, 90, 110, 95, 105],
            'genre': [1, 2, 1, 3, 2],  
            'rating': [1, 2, 2, 3, 1],  
            'country': [1, 1, 2, 2, 3],  
            'gross': [500, 600, 700, 800, 900]
        }
        df = pd.DataFrame(data)

        X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['gross']), df['gross'], test_size=0.2, random_state=42)

        model.fit(X_train, y_train)

        train_preds = model.predict(X_train)
        train_rmse = mean_squared_error(y_train, train_preds, squared=False)
        test_preds = model.predict(X_test)
        test_rmse = mean_squared_error(y_test, test_preds, squared=False)

        train_rmse_sk = sk_mean_squared_error(y_train, train_preds, squared=False)
        test_rmse_sk = sk_mean_squared_error(y_test, test_preds, squared=False)

        self.assertAlmostEqual(train_rmse, train_rmse_sk, places=6)
        self.assertAlmostEqual(test_rmse, test_rmse_sk, places=6)

if __name__ == '__main__':
    unittest.main()

