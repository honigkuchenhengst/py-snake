import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('KI1Ergebnisse.csv')
data_1 =  (data.copy().drop('boardgroesse',axis=1)
           .drop('wiederholungen',axis=1)
           .drop('gesamtlaufzeit(s)',axis=1))
           #.drop('closedListglobal',axis=1))
data_1 = data_1[data_1['alg'].isin(['idaStar'])]
data_1 = data_1[data_1['heuristik'].isin(['m'])]
data_1 = data_1[data_1['closedListglobal'].isin(['no'])]

data_1.insert(1,'wegProFrucht',0)
for row in data_1.iterrows():
    data_1['wegProFrucht'] = data_1['gesamtweg']/data_1['gesamtscore']
print(data_1)


plt.title('ida*,manhattan,keineGlobaleClosedList')
sns.heatmap(data_1.pivot(index='gewichtungFood',columns='gewichtungSnake', values='wegProFrucht'))
plt.show()

data_2 =  (data.copy().drop('boardgroesse',axis=1)
           .drop('wiederholungen',axis=1)
           .drop('gesamtlaufzeit(s)',axis=1))
           #.drop('closedListglobal',axis=1))
data_2 = data_2[data_2['alg'].isin(['idaStar'])]
data_2 = data_2[data_2['heuristik'].isin(['e'])]
data_2 = data_2[data_2['closedListglobal'].isin(['no'])]

data_2.insert(1,'wegProFrucht',0)
for row in data_2.iterrows():
    data_2['wegProFrucht'] = data_2['gesamtweg']/data_2['gesamtscore']
print(data_2)
plt.title('ida*,euklid,keineGlobaleClosedList')
sns.heatmap(data_2.pivot(index='gewichtungFood',columns='gewichtungSnake', values='wegProFrucht'))
plt.show()

data_3 =  (data.copy().drop('boardgroesse',axis=1)
           .drop('wiederholungen',axis=1)
           .drop('gesamtlaufzeit(s)',axis=1))
           #.drop('closedListglobal',axis=1))
data_3 = data_3[data_3['alg'].isin(['idaStar'])]
data_3 = data_3[data_3['heuristik'].isin(['e'])]
data_3 = data_3[data_3['closedListglobal'].isin(['yes'])]

data_3.insert(1,'wegProFrucht',0)
for row in data_3.iterrows():
    data_3['wegProFrucht'] = data_3['gesamtweg']/data_3['gesamtscore']
print(data_3)
plt.title('ida*,euklid,GlobaleClosedList')
sns.heatmap(data_3.pivot(index='gewichtungFood',columns='gewichtungSnake', values='wegProFrucht'))
plt.show()

data_4 =  (data.copy().drop('boardgroesse',axis=1)
           .drop('wiederholungen',axis=1)
           .drop('gesamtlaufzeit(s)',axis=1))
           #.drop('closedListglobal',axis=1))
data_4 = data_4[data_4['alg'].isin(['idaStar'])]
data_4 = data_4[data_4['heuristik'].isin(['m'])]
data_4 = data_4[data_4['closedListglobal'].isin(['yes'])]

data_4.insert(1,'wegProFrucht',0)
for row in data_4.iterrows():
    data_4['wegProFrucht'] = data_4['gesamtweg']/data_4['gesamtscore']
print(data_4)
plt.title('ida*,manhattan,GlobaleClosedList')
sns.heatmap(data_4.pivot(index='gewichtungFood',columns='gewichtungSnake', values='wegProFrucht'))
plt.show()


data_5 =  (data.copy().drop('boardgroesse',axis=1)
           .drop('wiederholungen',axis=1)
           .drop('gesamtlaufzeit(s)',axis=1))
           #.drop('closedListglobal',axis=1))
data_5 = data_5[data_5['alg'].isin(['aStar'])]
data_5 = data_5[data_5['heuristik'].isin(['m'])]
data_5 = data_5[data_5['closedListglobal'].isin(['no'])]

data_5.insert(1,'wegProFrucht',0)
for row in data_5.iterrows():
    data_5['wegProFrucht'] = data_5['gesamtweg']/data_5['gesamtscore']
print(data_5)


plt.title('a*,manhattan,keineGlobaleClosedList')
sns.heatmap(data_5.pivot(index='gewichtungFood',columns='gewichtungSnake', values='wegProFrucht'))
plt.show()

data_6 =  (data.copy().drop('boardgroesse',axis=1)
           .drop('wiederholungen',axis=1)
           .drop('gesamtlaufzeit(s)',axis=1))
           #.drop('closedListglobal',axis=1))
data_6 = data_6[data_6['alg'].isin(['aStar'])]
data_6 = data_6[data_6['heuristik'].isin(['e'])]
data_6 = data_6[data_6['closedListglobal'].isin(['no'])]

data_6.insert(1,'wegProFrucht',0)
for row in data_6.iterrows():
    data_6['wegProFrucht'] = data_6['gesamtweg']/data_6['gesamtscore']
print(data_6)
plt.title('a*,euklid,keineGlobaleClosedList')
sns.heatmap(data_6.pivot(index='gewichtungFood',columns='gewichtungSnake', values='wegProFrucht'))
plt.show()

data_7 =  (data.copy().drop('boardgroesse',axis=1)
           .drop('wiederholungen',axis=1)
           .drop('gesamtlaufzeit(s)',axis=1))
           #.drop('closedListglobal',axis=1))
data_7 = data_7[data_7['alg'].isin(['aStar'])]
data_7 = data_7[data_7['heuristik'].isin(['e'])]
data_7 = data_7[data_7['closedListglobal'].isin(['yes'])]

data_7.insert(1,'wegProFrucht',0)
for row in data_7.iterrows():
    data_7['wegProFrucht'] = data_7['gesamtweg']/data_7['gesamtscore']
print(data_7)
plt.title('a*,euklid,GlobaleClosedList')
sns.heatmap(data_7.pivot(index='gewichtungFood',columns='gewichtungSnake', values='wegProFrucht'))
plt.show()

data_8 =  (data.copy().drop('boardgroesse',axis=1)
           .drop('wiederholungen',axis=1)
           .drop('gesamtlaufzeit(s)',axis=1))
           #.drop('closedListglobal',axis=1))
data_8 = data_8[data_8['alg'].isin(['aStar'])]
data_8 = data_8[data_8['heuristik'].isin(['m'])]
data_8 = data_8[data_8['closedListglobal'].isin(['yes'])]

data_8.insert(1,'wegProFrucht',0)
for row in data_8.iterrows():
    data_8['wegProFrucht'] = data_8['gesamtweg']/data_8['gesamtscore']
print(data_8)
plt.title('a*,manhattan,GlobaleClosedList')
sns.heatmap(data_8.pivot(index='gewichtungFood',columns='gewichtungSnake', values='wegProFrucht'))
plt.show()
