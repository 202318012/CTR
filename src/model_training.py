from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from helper import make_pickle
import os

def evaluation(X_train, X_test, y_train, y_test, models, params=False):

    try :

        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            # para=param[list(models.keys())[i]]

            # gs = GridSearchCV(model,para,cv=3)
            # gs.fit(X_train,y_train)

            # model.set_params(**gs.best_params_)
            # model = model()
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    
    except Exception as e:
        print('Error in evaluation() \nException: ', e )

def train_model(train, test):

    try:

        X_train, X_test = train[:,:-1], test[:,:-1]
        y_train, y_test = train[:,-1], test[:,-1]

        models = {
            "Random Forest": RandomForestRegressor(),   
            "Linear Regression": LinearRegression(),
            "SVR": SVR(),
            "KNN": KNeighborsRegressor() 
        }

        # params={        
        #     "Random Forest":{
        #         'max_features':['sqrt','log2'],
        #         'n_estimators': [8,16,32,64,128,256]
        #     },
        #     "Linear Regression":{},
        #     "KNN": {
        #         'n_neighbors': [3,5,7,9]
        #     },
        #     "SVR":{
        #         'kernel': ['rbf', 'linear'], 
        #         'C': [1, 5, 10],
        #     }
        # }

        model_report:dict=evaluation(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models)
            
        ## To get best model score from dict
        best_model_score = max(sorted(model_report.values()))

        ## To get best model name from dict

        best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
        ]
        best_model = models[best_model_name]

        path = os.path.join('datafiles', 'model.pkl')

        print(best_model)

        make_pickle(path, best_model)

    except Exception as e:
        print('Error in train_model() \nException: ', e)