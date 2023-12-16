import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
from vega_datasets import data
from PIL import Image

# Configura el título de la página i favicon
st.set_page_config(page_title="Shooting Similarity", page_icon="detective.png", layout="wide")
st.title('🕵️Similitud Jugadores')
st.subheader('📌Descubre los jugadores más similares entre si respecto a su eficacia en el lanzamiento en la Liga Asobal.')
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    imageasobal = Image.open('apple-touch-icon.png')
    st.image(imageasobal)

#-------------------------------------
df = pd.read_excel('DatasetJugadoresAsobal.xlsx')
df1 = pd.read_excel("DatasetJugadoresAsobal2324.xlsx")
#-------------------------------------
#-------------------------------------

# Librerías

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import numpy as np

from matplotlib import pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings(action="ignore")

#---------------------------------------------------------------------------------------------------------------------------------

#Temporada Actual:
st.write('Temporada 23-24')

#Cambiar orden posicion metricas object:
df1.insert(1,'Jugador', df1.pop("Jugador"))
df1.insert(2,'Posicion', df1.pop("Posicion"))

#Eliminar columnas:
df1.drop(columns='Nº', inplace=True)
df1.drop(columns='Equipo', inplace=True)
df1.drop(columns='Posicion', inplace=True)
df1.drop(columns='Temporada', inplace=True)


X, y = df1.iloc[:, 1:len(df1.columns)].values, df1.iloc[:, 0].values

X_std = StandardScaler().fit_transform(X)

pca = PCA(n_components = len(df1.columns)-1)
pca.fit(X_std)
X_pca = pca.transform(X_std)

print("Shape x_PCA: ", X_pca.shape)
expl = pca.explained_variance_ratio_

for x in range(0, len(df1.columns), 2):
    print("Explained Variance: " + str(x) + " components:", sum(expl[0:x]))

plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Dimensions')
plt.ylabel('Explained Variance')
plt.show()

N_COMP = 8
columns = []

for col in range(1, N_COMP+1, 1):
    columns.append("PCA" + str(col))

df1_pca_resultado = pd.DataFrame(data=X_pca[:,0:N_COMP], columns=columns, index = y)

df1_pca_resultado.head()

corr_matrix = df1_pca_resultado.T.corr(method='pearson')

## Conseguir lista de equipos
Players = df1['Jugador'].unique()

## Create the select box
selected_player = st.selectbox('Escoge jugador:', Players)

## Filter the data
filtered_data = df1[df1['Jugador'] == selected_player]




def GetSimilarPlayers(Jugador, numPlayers, corr_matrix):

    SimPlayers = pd.DataFrame(columns = ['Jugador', 'Similar Player', 'Correlation Factor'])

    i = 0
    for i in range(0, numPlayers):
        row = corr_matrix.loc[corr_matrix.index == Jugador].squeeze()

        SimPlayers.at[i, 'Jugador'] = Jugador
        SimPlayers.at[i, 'Similar Player'] = row.nlargest(i+2).sort_values(ascending=True).index[0]
        SimPlayers.at[i, 'Correlation Factor'] = row.nlargest(i+2).sort_values(ascending=True)[0]

        i = i+1

    return SimPlayers

Jugador = 'Faruk Yusuf'
NumPlayers = 5

# Check if a player is selected
if selected_player:
    # Call the function with the selected player
    df_correlatedPlayers1 = GetSimilarPlayers(selected_player, NumPlayers, corr_matrix)

    # Display the resulting DataFrame
    st.write(df_correlatedPlayers1)
    
st.caption("🔎Fuente: Asobal")
st.divider()
#---------------------------------------------------------------------------------------------------------------------------------

#Temporada Anterior:
st.write('Temporada 22-23')
#Cambiar orden posicion metricas object:
df.insert(1,'Jugador', df.pop("Jugador"))
df.insert(2,'Posicion', df.pop("Posicion"))

#Eliminar columnas:
df.drop(columns='Nº', inplace=True)
df.drop(columns='Equipo', inplace=True)
df.drop(columns='Posicion', inplace=True)
df.drop(columns='Temporada', inplace=True)


X, y = df.iloc[:, 1:len(df.columns)].values, df.iloc[:, 0].values

X_std = StandardScaler().fit_transform(X)

pca = PCA(n_components = len(df.columns)-1)
pca.fit(X_std)
X_pca = pca.transform(X_std)

print("Shape x_PCA: ", X_pca.shape)
expl = pca.explained_variance_ratio_

for x in range(0, len(df.columns), 2):
    print("Explained Variance: " + str(x) + " components:", sum(expl[0:x]))

plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Dimensions')
plt.ylabel('Explained Variance')
plt.show()

N_COMP = 8
columns = []

for col in range(1, N_COMP+1, 1):
    columns.append("PCA" + str(col))

df_pca_resultado = pd.DataFrame(data=X_pca[:,0:N_COMP], columns=columns, index = y)

df_pca_resultado.head()

corr_matrix = df_pca_resultado.T.corr(method='pearson')

## Conseguir lista de equipos
Players = df['Jugador'].unique()

## Create the select box
selected_player = st.selectbox('Escoge jugador:', Players)

## Filter the data
filtered_data = df[df['Jugador'] == selected_player]




def GetSimilarPlayers(Jugador, numPlayers, corr_matrix):

    SimPlayers = pd.DataFrame(columns = ['Jugador', 'Similar Player', 'Correlation Factor'])

    i = 0
    for i in range(0, numPlayers):
        row = corr_matrix.loc[corr_matrix.index == Jugador].squeeze()

        SimPlayers.at[i, 'Jugador'] = Jugador
        SimPlayers.at[i, 'Similar Player'] = row.nlargest(i+2).sort_values(ascending=True).index[0]
        SimPlayers.at[i, 'Correlation Factor'] = row.nlargest(i+2).sort_values(ascending=True)[0]

        i = i+1

    return SimPlayers

Jugador = 'Faruk Yusuf'
NumPlayers = 5

# Check if a player is selected
if selected_player:
    # Call the function with the selected player
    df_correlatedPlayers = GetSimilarPlayers(selected_player, NumPlayers, corr_matrix)

    # Display the resulting DataFrame
    st.write(df_correlatedPlayers)


st.caption("🔎Fuente: Asobal")


#------------------------------------------------------------


