from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import VarianceThreshold
import pandas as pd
import numpy as np
from helper import make_pickle
import os
import traceback

def process_data(df):

    try:
    
        numerical_columns = df.select_dtypes(include=["int64", 'float64']).columns.tolist()

        categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()
        unwanted_num = {'Gender', 'Education Level', 'Income Level'}

        nominal_cols = [ele for ele in categorical_columns if ele not in unwanted_num]
        ordinal_cols = [ele for ele in categorical_columns if ele in unwanted_num]
        numerical_columns = df.select_dtypes(include=["int64", 'float64']).columns.tolist()

        numerical_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())
        ])

        nominal_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(drop='first'))
        ])

        ordinal_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('label', OrdinalEncoder())
        ])

        preprocessor = ColumnTransformer(
            transformers=[
                ('ordinal', ordinal_pipeline, ordinal_cols),
                ('nominal', nominal_pipeline, nominal_cols),
                ('num', numerical_pipeline, numerical_columns),
            ],
            remainder = 'passthrough'
        )

        return preprocessor
    
    except Exception as e:
        print('Error in process_data() pipeline \nException: ', e)


def transform_data(train_path, test_path):

    try:
        train = pd.read_csv(train_path)
        test = pd.read_csv(test_path)

         
        train = train.drop(columns= ['User ID', 'Top Interests'])
        test = test.drop(columns= ['User ID', 'Top Interests'])
        

        target_variable = 'Conversion Rates'

        train_features = train.drop(columns=[target_variable], axis=1)
        test_features = test.drop(columns=[target_variable], axis=1)

        train_target = train[target_variable]
        test_target = test[target_variable]

        preprocessor = process_data(train_features)

        train_features = preprocessor.fit_transform(train_features)
        test_features = preprocessor.fit_transform(test_features)

        train = np.c_[train_features, np.array(train_target)]
        test = np.c_[test_features, np.array(test_target)]

        
        path = os.path.join('datafiles', 'preprocessor.pkl')        

        pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor)])

        make_pickle(path, pipeline)

        return train, test, pipeline


    except Exception as e:
        print('Error in transform_data() \nException: ', e, traceback.print_exc())

