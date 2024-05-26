import pandas as pd
from sklearn.model_selection import train_test_split
from feature_engineering import transform_data
import os
from model_training import train_model

def ingest_data(file):

    try:

        path = os.path.join('datafiles', file)

        df = pd.read_csv(path)

        data_path = os.path.join('datafiles', 'data.csv')
        df.to_csv(data_path, index=False, header=True)
        train, test = train_test_split(df, test_size=0.2, random_state=42)

        train_path = os.path.join('datafiles', 'train.csv')
        test_path = os.path.join('datafiles', 'test.csv')

        train.to_csv(train_path, index = False)
        test.to_csv(test_path, index = False)

        return train_path, test_path
    
    except Exception as e:
        print('Error in ingest_data() \nException: ', e)
        


if __name__ == '__main__':

    try:
        file = 'user_profiles_for_ads.csv'
        train, test = ingest_data(file)

        train, test, engineered = transform_data(train, test)

        train_model(train, test)

    except Exception as e:

        print('Error in data ingestion \nException ', e)