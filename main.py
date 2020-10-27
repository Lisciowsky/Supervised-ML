'''This script has been used for supervised machine learning study. It can be
   adjusted if needed. In the script five popular classifcators were used :
   SVM, Logistic Regression, Random Forest, Naive Bayes, Decision Tree'''

# =============================================================================
#                           Imports
# =============================================================================

import numpy as np
import os
import pandas as pd

#importing classificators / sklearn

from sklearn.feature_selection import f_classif
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif

#Classificators
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix



    #enter directory location, where the csv file is located
directory = '/home/kuba/Windows_Old_Staff/ML_THESIS/NBA_python'
os.chdir(directory)
    
        
df = pd.read_csv('MERGED_FINAL_80_16_po_obrobce_dummie.csv', index_col = 0)
        
df = df[['FG', 'FGA', '3P',
        '3PA', '2P', '2PA', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST',
        'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PER',
        'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'USG%', 'OWS', 'DWS',
        'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP', 'hall_of_fame', 'POS_C', 
        'POS_PF', 'POS_PG', 'POS_SF', 'POS_SG']]

X = df.drop('hall_of_fame', axis = 1).values
y = df.iloc[:,34].values

    #Selecitng the best features from the dataset

best_features = SelectKBest(score_func = f_classif, k = 10)
fit = best_features.fit(X,y)
features = fit.transform(X)
features_df = pd.DataFrame(features)
df_pos = df[['POS_C', 'POS_PF', 'POS_PG', 'POS_SF', 'POS_SG']]
features_df = pd.concat([features_df, df_pos], axis=1)
ready = features_df.values




# Train Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(ready, y, test_size=0.25, random_state = 0)
print('train split correctly')

    #Using Standard Scaler
from sklearn.preprocessing import StandardScaler
# from sklearn.preprocessing import MinMaxScaler
# min_max_scaler = MinMaxScaler()
sc = StandardScaler()
sc.fit(X_test)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
# X_test_std = min_max_scaler.fit_transform(X_test)
# X_train_std = min_max_scaler.fit(X_train)
print('Scaling done')


    #Classificators
rf = RandomForestClassifier(random_state = 0)
dt = DecisionTreeClassifier(random_state = 0)
naiv = GaussianNB()
log = LogisticRegression(random_state = 0)
svm = SVC(random_state = 0)

    #fitting classificators with the train data
rf.fit(X_train_std, y_train)
dt.fit(X_train_std, y_train)
naiv.fit(X_train_std, y_train)
log.fit(X_train_std, y_train)
svm.fit(X_train_std, y_train)
print('fitting done')

    #choose the right inputs in the zip function, depending on the study | Train or Test
train_x = [X_train_std]
train_y = [y_train]
test_x = [X_test_std]
test_y = [y_test]

    #creating a confusion matrix for each classificator
for a,b in zip(train_x, train_y):
    
    y_pred_rf = rf.predict(a)
    cm_rf_one = confusion_matrix(b, y_pred_rf)
    
    #DecisionTree
    y_pred_dt = dt.predict(a)
    cm_dt_one = confusion_matrix(b, y_pred_dt)
    
    #NAIVE BAYES
    y_pred_naiv = naiv.predict(a)
    cm_naiv_one = confusion_matrix(b, y_pred_naiv)
    
    #Logistic Regression
    y_pred_log = log.predict(a)
    cm_log_one = confusion_matrix(b, y_pred_log)
    
    #SVM
    y_pred_svm = svm.predict(a)
    cm_svm_one = confusion_matrix(b, y_pred_svm)
    print('done')



    # cm_rf_one = first_second(a,b)[0]
    # cm_dt_one = first_second(a,b)[1]
    # cm_naiv_one = first_second(a,b)[2]
    # cm_log_one = first_second(a,b)[3]
    # cm_svm_one = first_second(a,b)[4]
    
cm_rf_one_dimension = []
cm_dt_one_dimension = []
cm_naiv_one_dimension = []
cm_log_one_dimension = []
cm_svm_one_dimension = []




#creating a list, with the confusion matrix results
lists = [cm_dt_one_dimension, cm_log_one_dimension, cm_naiv_one_dimension, cm_rf_one_dimension, cm_svm_one_dimension]
dimensions = [cm_dt_one, cm_log_one, cm_naiv_one, cm_rf_one, cm_svm_one]

klassifi = ['Decision Tree','Logistic regression','Naiv','Random Forest','SVM']
# =============================================================================
# creation of dataframe with classificators confusion matrix results.
# =============================================================================
True_negative = []
False_negative = []
True_postivie = []
False_positive = []
merged_df = pd.DataFrame(columns = ['classificator','True_negative','True_postivie',
                                    'False_positive', 'False_negative'])


for (dimension, lista, klass) in zip(dimensions, lists, klassifi):

    True_negative = []
    False_negative = []
    True_postivie = []
    False_positive = []
    
    True_negative.append(dimension[0,0])
    False_negative.append(dimension[1,0])
    True_postivie.append(dimension[1,1])
    False_positive.append(dimension[0,1])
    worterbuch = {'classificator': klass, 'True_negative': True_negative, 'True_postivie' : True_postivie,
          'False_positive' : False_positive, 'False_negative': False_negative,}
    curr_df = pd.DataFrame(worterbuch)
    merged_df = pd.merge(left = merged_df, right = curr_df, how = 'outer') 
print('merged df has been created')



    
