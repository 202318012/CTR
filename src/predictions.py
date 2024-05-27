import os
import pickle
from src.helper import get_pickle
import pandas as pd
from numpy import round

def predict(X_test):
    try:
        
        preprocessor_path = os.path.join('datafiles', 'preprocessor.pkl')
        model_path = os.path.join('datafiles', 'model.pkl')

        model=get_pickle(model_path)
        preprocessor=get_pickle(preprocessor_path)
            
        tranformed_df = preprocessor.transform(X_test)

        y_pred = model.predict(tranformed_df)[0]

        print('X_test:', X_test)
        print('predicted: ', y_pred)

        return round(y_pred, 4)

    except Exception as e:
        print('Error in predict() \nException: ',e)