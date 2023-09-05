import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression

from sklearn.neighbors import  KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging


models = {
    "Random Forest": RandomForestRegressor(),
    "Decision Tree": DecisionTreeRegressor(),
    "Gradient Boosting": GradientBoostingRegressor(),
    "Linear Regression": LinearRegression(),
    "XGBRegressor": XGBRegressor(),
    "CatBoosting Regressor": CatBoostRegressor(verbose=False),
    "AdaBoost Regressor": AdaBoostRegressor(),
}




params = {
                "Decision Tree": {
                    'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest": {
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],

                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },
                "Gradient Boosting": {
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate': [.1, .01, .05, .001],
                    'subsample': [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },
                "Linear Regression": {},
                "XGBRegressor": {
                    'learning_rate': [.1, .01, .05, .001],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },
                "CatBoosting Regressor": {
                    'depth': [6, 8, 10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor": {
                    'learning_rate': [.1, .01, 0.5, .001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                }

            }
# print(params[list(models.keys())[0]])
# for key,values in params.items():
#     print(key,":",values)
# i=0
# model = list(models.values())[i]
# para = params[list(models.keys())[i]]

# k = list(models.items())

# for key in models.keys():
    # model = models[key]
    # para = params[key]
    # print('model:',model,'\t','para:',para)


model_report_1 = {'Random Forest': 0.8571035867960888, 'Decision Tree': 0.7444192803581263,
                'Gradient Boosting': 0.8616039087289575, 'Linear Regression': 0.8629895363812159,
                'XGBRegressor': 0.8521494413345255, 'CatBoosting Regressor': 0.8634067918235375,
                'AdaBoost Regressor': 0.8207438185028915}

# best_model_score_1 : 0.8634067918235375

model_report_2 = {'Random Forest': 0.8566081043459411, 'Decision Tree': 0.7469347083162696,
                'Gradient Boosting': 0.8634126981230519, 'Linear Regression': 0.8629895363812159,
                'XGBRegressor': 0.8521494413345255, 'CatBoosting Regressor': 0.8634067918235375,
                'AdaBoost Regressor': 0.8207327838230718}

# best_model_name: Gradient Boosting
# best_model_score: 0.8634126981230519
# r2_score: 0.8634126981230519




# best_model_score_1 = max(sorted(model_report.values()))
# print("best_model_score_1 :", best_model_score_1)
# # best_model_score_1 : 0.8634067918235375
#
# print('sorted dict values :',sorted(model_report.values()))
#
best_model_score_2 = max(model_report_1.values())
# print("best_model_score_2 :", best_model_score_2)
# # no need to sort the values
# # both 1 and 2 yields the same results
#
# print(max(model_report))
# # returns-> max:based on keys not values

# to get best model name from dict:
# best_model_name_1 = list(model_report.keys())[list(model_report.values()).index(best_model_score_2)]
# print('best_model_name_1 :', best_model_name_1)


def find_best_model_name_score(model_report):

    best_model_score = 0
    best_model_name = ''

    for key,value in model_report.items():
        if value > best_model_score:
            best_model_score = value
            best_model_name = key

    return (best_model_name,best_model_score)



# best_model_name,best_model_score = find_best_model_name_score(model_report)
# print('best_model_name:',best_model_name)
# print('best_model_score:',best_model_score)

report = {}
test_model_score ='00.00'
for key,value in models.items():
    model = value
    para = params[key]
    print(model,':',para)

    report[key] = test_model_score

print(report)

