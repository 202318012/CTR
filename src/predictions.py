import os
import pickle
from helper import get_pickle
import pandas as pd

def predict(X_test):
    try:
        
        preprocessor_path = os.path.join('datafiles', 'preprocessor.pkl')
        model_path = os.path.join('datafiles', 'model.pkl')

        model=get_pickle(model_path)
        preprocessor=get_pickle(preprocessor_path)
            
        tranformed_df = preprocessor.transform(X_test)

        y_pred = model.predict(tranformed_df)

        print('predicted: ', y_pred)

    except Exception as e:
        print('Error in predict() \nException: ',e)

if __name__ == '__main__':
    try:

        X_test = pd.DataFrame({'Age': ['25-34'], 'Gender': ['Male'], 'Location': ['Urban'], 'Language': ['Hindi'], 'Education Level': ['PhD'], 'Likes and Reactions': [8343], 'Followed Accounts': [307], 'Device Usage': ['Tablet'], 'Time Spent Online (hrs/weekday)': [3.7], 'Time Spent Online (hrs/weekend)': [4.2], 'Click-Through Rates (CTR)': [0.245], 'Ad Interaction Time (sec)': [83], 'Income Level': ['0-20k']})
        predict(X_test)


    except Exception as e:
        print('Error in predictions main(), \nException: ', e)