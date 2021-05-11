#FORWARDY

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



forwardy = []
for i in list(range(len(df))):
    if df['Pos'][i][0] == 'F':
        forwardy.append(df['Player'][i])

          
#df = df[~df['Player'].isin(forwardy)]

###Tylko centry w df-ie
df = df[df['Player'].isin(forwardy)]
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
# 
# =============================================================================
# =============================================================================
# 
# =============================================================================
# =============================================================================
# 
# =============================================================================


test = get_game_logs(df['Player'][0], df['poczatek_sezonu'][0], df['koniec_1_sezonu'][0])
data_frame = pd.DataFrame(columns = test.columns)
list_of_fail_forwards = []
counter = 0


for i in list(range(408,len(df))):
        print(df['Player'][i])
        start = df['poczatek_sezonu'][i]
        end = df['koniec_1_sezonu'][i]
        try:
            curr_data_frame = get_game_logs(df['Player'][i],start_date = start, end_date = end, playoffs = False)
        except (TypeError, AttributeError) as e:
                counter = counter + 1
                list_of_fail_forwards.append(df['Player'][i])
        pass
        data_frame = pd.merge(left = data_frame, right = curr_data_frame, how = 'outer')


#data_frame.to_csv('forwardy_sezon_1.csv')


# =============================================================================
# SCIAGA Z IMIONAMI
# =============================================================================
for i in list(range(len(df))):
        print(df['Player'][i])
        start = df['poczatek_sezonu'][i]
        end = df['koniec_1_sezonu'][i]
        try:
            curr_data_frame = get_game_logs(df['Player'][i],start_date = start, end_date = end, playoffs = False)
        except (TypeError, AttributeError) as e:
                counter = counter + 1
                list_of_fail_forwards.append(df['Player'][i])

        pass
        curr_data_frame.index = range(len(curr_data_frame))
        imie_gracza = pd.DataFrame(np.array(np.zeros(len(curr_data_frame))), columns = ['nazwa_gracza'])
        imie_gracza.replace(imie_gracza['nazwa_gracza'][0], df['Player'][i], inplace = True)
        curr_data_frame['nazwa_gracza'] = imie_gracza['nazwa_gracza']
        data_frame = pd.merge(left = data_frame, right = curr_data_frame, how = 'outer')





