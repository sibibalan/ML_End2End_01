import os
import sys

import numpy as np
import pandas as pd
# import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, grid_params):
    try:
        report = {}

        for key,value in models.items():
            model = value
            params = grid_params[key]

        # for i in range(len(list(models))):
        #     model = list(models.values())[i]
        #     para = params[list(models.keys())[i]]

            gs = GridSearchCV(model, params, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[key] = test_model_score
            # report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)

def find_best_model_name_score(model_report):
    '''
    find best model name and its score, based on the r2_score
    :param model_report:
    :return: best_model_name,best_model_score
    '''
    best_model_score = 0
    best_model_name = ''

    for key,value in model_report.items():
        if value > best_model_score:
            best_model_score = value
            best_model_name = key

    return (best_model_name,best_model_score)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)