# =============================================================================
# Quick Crypto Portfolio
# =============================================================================
import requests
import pandas as pd
import numpy as np
import bs4 as bs4
from basketball_reference_scraper.players import get_stats, get_game_logs
from urllib.request import urlopen
import pandas as pd
import numpy as np
import os



path = 'C:/Users/kuba/Desktop/Pobrane/NBA_python'
os.chdir(path)


df = pd.read_excel('Cala_lista_graczy.xlsx')

redukcja_df = []
for i in list(range(len(df))):
     if "*" in df['Player'][i]:
         redukcja_df.append(df['Player'][i])

df = df[~df['Player'].isin(redukcja_df)]


df.index = list(range(len(df)))

lista_graczy = []
for i in list(range(len(df))):
    if df['From'][i] > 1980 and df['To'][i] < 2016:
        lista_graczy.append(df['Player'][i])

df = df[df['Player'].isin(lista_graczy)]

df.index = range(len(df))



lista_centrow = []
for i in list(range(len(df))):
    if df['Pos'][i][0] == 'C':
        lista_centrow.append(df['Player'][i])

          
#df = df[~df['Player'].isin(lista_centrow)]

###Tylko centry w df-ie
df = df[df['Player'].isin(lista_centrow)]
#reset indexu na 12345
df.index = range(len(df))

df['poczatek_sezonu'] = np.zeros((len(df)))
df['koniec_1_sezonu'] = np.zeros((len(df)))
df['poczatek_2_sezonu'] = np.zeros((len(df)))
df['koniec_2_sezonu'] = np.zeros((len(df)))
df['poczatek_3_sezonu'] = np.zeros((len(df)))
df['koniec_3_sezonu'] = np.zeros((len(df)))

# =============================================================================
# USTALANIE KONKRETNYCH DAT
# =============================================================================

poczatek_sezonu = '-10-10'
koniec_sezonu = '-06-01'

#poczatek sezonu
for i in range(len(df)):
    if (df['To'][i] - df['From'][i]) >= 3:
        df['poczatek_sezonu'][i] = (str(df['From'][i] - 1) + poczatek_sezonu)


#df['koniec_1_sezonu'] = np.zeros((len(df)))

for i in range(len(df)):
    if (df['To'][i] - df['From'][i]) >= 3:
        df['koniec_1_sezonu'][i] = (str(df['From'][i]) + koniec_sezonu)


#df['poczatek_2_sezonu'] = np.zeros((len(df)))

for i in range(len(df)):
    if (df['To'][i] - df['From'][i]) >= 3:
        df['poczatek_2_sezonu'][i] = (str(df['From'][i]) + poczatek_sezonu)


#df['koniec_2_sezonu'] = np.zeros((len(df)))

for i in range(len(df)):
    if (df['To'][i] - df['From'][i]) >= 3:
        df['koniec_2_sezonu'][i] = (str(df['From'][i] + 1) + koniec_sezonu)

#df['poczatek_3_sezonu'] = np.zeros((len(df)))

for i in range(len(df)):
    if (df['To'][i] - df['From'][i]) >= 3:
        df['poczatek_3_sezonu'][i] = (str(df['From'][i] + 1) + poczatek_sezonu)


#df['koniec_3_sezonu'] = np.zeros((len(df)))

for i in range(len(df)):
    if (df['To'][i] - df['From'][i]) >= 3:
        df['koniec_3_sezonu'][i] = (str(df['From'][i] + 2) + koniec_sezonu)
# =============================================================================
# USTALANIE KONKRETNYCH DAT
# =============================================================================


#Wywalic tych co nie grali co najmniej 3 sezony
# =============================================================================
df.replace(0, np.NaN, inplace = True)
df.dropna(inplace = True)
# =============================================================================
df.index = range(len(df))

# =============================================================================
# for i in range(len(df)):
#     df['poczatek_sezonu'][i]
#     start = df['poczatek_sezonu'][i]
#     end = df['koniec_1_sezonu'][i]
# 
# #CENTRY DF
# for i in range(2):
#     try:
#         print(df['poczatek_sezonu'][i])
#         start = df['poczatek_sezonu'][i]
#         end = df['koniec_1_sezonu'][i]
#         curr_data_frame = get_game_logs(df['Player'][i],start_date = start, end_date = end, playoffs = False)
#     except:
#         pass
#     data_frame = pd.merge(left = data_frame, right = curr_data_frame, how = 'outer')
# 
# #kolumny = data_frame.columns 
# 
# 
# 
#    
#                 for i in xrange(0,960):
#     try:
#         ... run your code
#     except:
#         pass      
#                       
#                       
#                      
# start = '1984-01-01'
# end = '1985-06-01'
# mikel2 = get_game_logs('Michael Jordan',start_date = start, end_date = end, playoffs = False)
# 
# 
# 
# 
# 
# #data_frame.drop('+/-', axis = 1, inplace = True)
# 
# 
# for i in range(2):
#     print(df['Player'][i])
#     start = df['poczatek_sezonu'][i]
#     end = df['koniec_1_sezonu'][i]
# 
#     try:
#         curr_data_frame = get_game_logs(df['Player'][i],start_date = start, end_date = end, playoffs = False)
#     except (TypeError, AttributeError) as e:
#                     counter = counter + 1
#                     list_of_fail_centers.append(df['Player'][i])
#                     pass
# # =============================================================================
# =============================================================================
# DZIALADZIALADZIALADZIALADZIALADZIALADZIALADZIALADZIALADZIALADZIALADZIALADZIALA
# =============================================================================
#To działa
#               TWORZENIE PRZYKLADOWEGO DF-a w celu uzyskania kolumn


# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# # # # 



# =============================================================================
# DZIALADZIALADZIALADZIALADZIALADZIALADZIALADZIALADZIALADZIALADZIALA
# =============================================================================

#data_frame.drop('+/-', axis = 1, inplace = True)
# =============================================================================
# test = get_game_logs(df['Player'][0], df['poczatek_sezonu'][0], df['koniec_1_sezonu'][0])
# #data_frame = pd.DataFrame(columns = test.columns)
# list_of_fail_centers = []
# counter = 0
# ########################### POCZATEK SEZONU - KONIEC 1 SEZONU
# =============================================================================

# =============================================================================
# for i in list(range(144,len(df))):
#         print(df['Player'][i])
#         start = df['poczatek_sezonu'][i]
#         end = df['koniec_1_sezonu'][i]
#         try:
#             curr_data_frame = get_game_logs(df['Player'][i],start_date = start, end_date = end, playoffs = False)
#         except (TypeError, AttributeError) as e:
#                 counter = counter + 1
#                 list_of_fail_centers.append(df['Player'][i])
#         pass
#         data_frame = pd.merge(left = data_frame, right = curr_data_frame, how = 'outer')
# 
# #data_frame.to_csv('centry.csv')
# =============================================================================

######################### pczatek_2_sezonu - koniec_2_sezonu

# =============================================================================
# test = get_game_logs(df['Player'][0], df['poczatek_sezonu'][0], df['koniec_1_sezonu'][0])
# data_frame = pd.DataFrame(columns = test.columns)
# list_of_fail_centers = []
# counter = 0
# 
# 
# 
# 
# for i in list(range(144,len(df))):
#         print(df['Player'][i])
#         start = df['poczatek_2_sezonu'][i]
#         end = df['koniec_2_sezonu'][i]
#         try:
#             curr_data_frame = get_game_logs(df['Player'][i],start_date = start, end_date = end, playoffs = False)
#         except (TypeError, AttributeError) as e:
#                 counter = counter + 1
#                 list_of_fail_centers.append(df['Player'][i])
#         pass
#         data_frame = pd.merge(left = data_frame, right = curr_data_frame, how = 'outer')
# 
# data_frame.to_csv('centry_sezon_2.csv')
# 
# =============================================================================


#################### SEZON 3



test = get_game_logs(df['Player'][0], df['poczatek_sezonu'][0], df['koniec_1_sezonu'][0])
data_frame = pd.DataFrame(columns = test.columns)
list_of_fail_centers = []
counter = 0




for i in list(range(1)):
        print(df['Player'][i])
        start = df['poczatek_3_sezonu'][i]
        end = df['koniec_3_sezonu'][i]
        try:
            curr_data_frame = get_game_logs(df['Player'][i],start_date = start, end_date = end, playoffs = False)
        except (TypeError, AttributeError) as e:
                counter = counter + 1
                list_of_fail_centers.append(df['Player'][i])
        pass
        data_frame = pd.merge(left = data_frame, right = curr_data_frame, how = 'outer')



data_frame.to_csv('centry_sezon_3.csv')

