#House Price Predictor
##Dataset:
*The Dataset used for this House Price Predictor Model is Available as zip file in kaggle it have more than 10 column and 50000 rows 

Dataset link: #!/bin/bash
curl -L -o ~/Downloads/house-price-prediction-challenge.zip\
  https://www.kaggle.com/api/v1/datasets/download/anmolkumar/house-price-prediction-challenge

##Exploratory Data Analysis:
 *The Dataset is aldready cleaned so I didn't go through EDA part

 ##Feature Engineering :
 *Here the key matter which increases the accuracy massively is Feature Engineering
 *Here I have  used one hot encoding with column transfer for categorial columns to convert them to a numerical values
 *In ADDRESS column there are different set of district are there so i have select the district which have a value count more than 50 and encoded them by One Hot Encoder
 *No new Feature had been created

 ##Model Used:
 * The Model used for this Dataset is Random Forest
 * Other than this the Dataset well go with linear regression with regularization and hyper paramter tuning we can get better result
 * Here I didn't tuned the model the accuracy before and after tuning is mostly smiliar
 * The Metrices used to evaluvate the model are r2_score,mean_absolute_error

 
