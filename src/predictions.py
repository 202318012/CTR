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

# if __name__ == '__main__':
#     try:

#         X_test = pd.DataFrame({'Age': ['25-34'], 'Gender': ['Male'], 'Location': ['Urban'], 'Language': ['Hindi'], 'Education Level': ['PhD'], 'Likes and Reactions': [8343], 'Followed Accounts': [307], 'Device Usage': ['Tablet'], 'Time Spent Online (hrs/weekday)': [3.7], 'Time Spent Online (hrs/weekend)': [4.2], 'Click-Through Rates (CTR)': [24], 'Ad Interaction Time (sec)': [83], 'Income Level': ['0-20k']})
#         predict(X_test)


#     except Exception as e:
#         print('Error in predictions main(), \nException: ', e)